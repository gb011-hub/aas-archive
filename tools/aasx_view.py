"""AASX 파일을 열어 GitHub에서 바로 읽을 수 있는 열람 페이지(Markdown)를 만든다.

- AAS 메타모델 3.0 / 3.1 XML, JSON 형식을 모두 읽는다.
- 서브모델마다 접었다 펼 수 있는 표로 모든 요소(idShort · 종류 · 값 · semanticId)를 보여 준다.
- AASX 안에 썸네일 이미지가 있으면 꺼내서 페이지 맨 위에 보여 준다.
파이썬 표준 라이브러리만 사용한다.
"""
import json
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile
from urllib.parse import quote

KIND_KO = {
    "Property": "속성", "MultiLanguageProperty": "다국어 속성", "Range": "범위",
    "SubmodelElementCollection": "묶음", "SubmodelElementList": "목록", "File": "파일",
    "Blob": "바이너리", "ReferenceElement": "참조", "Entity": "엔티티",
    "RelationshipElement": "관계", "AnnotatedRelationshipElement": "관계",
    "Operation": "오퍼레이션", "Capability": "기능", "BasicEventElement": "이벤트",
}
ELEMENT_TAGS = {k[0].lower() + k[1:]: k for k in KIND_KO}
MAX_ROWS = 2000          # 너무 큰 모델은 페이지가 GitHub에서 열리지 않으므로 행 수를 제한 (약 400KB 이하)
THUMB_PX = 480           # 썸네일 긴 변 최대 픽셀
MAX_VALUE = 80


# ------------------------------------------------------------------ 공통 모델

def element(kind, id_short, value="", semantic="", children=None, desc=""):
    return {"kind": kind, "idShort": id_short or "", "value": value or "",
            "semantic": semantic or "", "children": children or [], "desc": desc or ""}


# ------------------------------------------------------------------ XML

def _local(tag):
    return tag.rsplit("}", 1)[-1]


def _child(node, name):
    for c in node:
        if _local(c.tag) == name:
            return c
    return None


def _text(node, name):
    c = _child(node, name)
    return (c.text or "").strip() if c is not None and c.text else ""


def _lang_text(node, prefer=("ko", "en")):
    """langStringTextType 묶음에서 한국어 → 영어 → 첫 값 순서로 고른다."""
    if node is None:
        return ""
    found = {}
    for ls in node:
        lang = _text(ls, "language")
        txt = _text(ls, "text")
        if txt:
            found.setdefault(lang.lower()[:2], txt)
    for p in prefer:
        if p in found:
            return found[p]
    return next(iter(found.values()), "")


def _semantic_xml(node):
    sid = _child(node, "semanticId")
    if sid is None:
        return ""
    keys = _child(sid, "keys")
    if keys is None:
        return ""
    vals = [_text(k, "value") for k in keys]
    return vals[-1] if vals else ""


def _xml_element(node):
    kind = ELEMENT_TAGS.get(_local(node.tag))
    if not kind:
        return None
    e = element(kind, _text(node, "idShort"), semantic=_semantic_xml(node),
                desc=_lang_text(_child(node, "description")))
    if kind == "Property":
        e["value"] = _text(node, "value")
    elif kind == "MultiLanguageProperty":
        e["value"] = _lang_text(_child(node, "value"))
    elif kind == "Range":
        lo, hi = _text(node, "min"), _text(node, "max")
        e["value"] = f"{lo} ~ {hi}" if (lo or hi) else ""
    elif kind in ("File", "Blob"):
        e["value"] = _text(node, "value") if kind == "File" else _text(node, "contentType")
    elif kind == "ReferenceElement":
        v = _child(node, "value")
        keys = _child(v, "keys") if v is not None else None
        e["value"] = " / ".join(_text(k, "value") for k in keys) if keys is not None else ""
    container = None
    if kind in ("SubmodelElementCollection", "SubmodelElementList"):
        container = _child(node, "value")
    elif kind == "Entity":
        container = _child(node, "statements")
    if container is not None:
        e["children"] = [c for c in (_xml_element(x) for x in container) if c]
    return e


def _parse_xml(data):
    root = ET.fromstring(data)
    model = {"shells": [], "submodels": []}
    for node in root.iter():
        name = _local(node.tag)
        if name == "assetAdministrationShell":
            info = _child(node, "assetInformation")
            model["shells"].append({
                "idShort": _text(node, "idShort"), "id": _text(node, "id"),
                "assetKind": _text(info, "assetKind") if info is not None else "",
                "globalAssetId": _text(info, "globalAssetId") if info is not None else "",
                "desc": _lang_text(_child(node, "description")),
            })
        elif name == "submodel":
            elems = _child(node, "submodelElements")
            model["submodels"].append({
                "idShort": _text(node, "idShort"), "id": _text(node, "id"),
                "semantic": _semantic_xml(node), "desc": _lang_text(_child(node, "description")),
                "elements": [c for c in (_xml_element(x) for x in elems) if c] if elems is not None else [],
            })
    return model


# ------------------------------------------------------------------ JSON

def _lang_json(items, prefer=("ko", "en")):
    if not isinstance(items, list):
        return ""
    found = {}
    for ls in items:
        if isinstance(ls, dict) and ls.get("text"):
            found.setdefault(str(ls.get("language", "")).lower()[:2], ls["text"])
    for p in prefer:
        if p in found:
            return found[p]
    return next(iter(found.values()), "")


def _semantic_json(obj):
    keys = (obj.get("semanticId") or {}).get("keys") or []
    return keys[-1].get("value", "") if keys else ""


def _json_element(obj):
    kind = obj.get("modelType")
    if isinstance(kind, dict):           # 구버전 표기
        kind = kind.get("name")
    if kind not in KIND_KO:
        return None
    e = element(kind, obj.get("idShort"), semantic=_semantic_json(obj), desc=_lang_json(obj.get("description")))
    v = obj.get("value")
    if kind == "Property":
        e["value"] = "" if v is None else str(v)
    elif kind == "MultiLanguageProperty":
        e["value"] = _lang_json(v)
    elif kind == "Range":
        lo, hi = obj.get("min", ""), obj.get("max", "")
        e["value"] = f"{lo} ~ {hi}" if (lo or hi) else ""
    elif kind == "File":
        e["value"] = v or ""
    elif kind == "Blob":
        e["value"] = obj.get("contentType", "")
    elif kind == "ReferenceElement" and isinstance(v, dict):
        e["value"] = " / ".join(k.get("value", "") for k in v.get("keys", []))
    if kind in ("SubmodelElementCollection", "SubmodelElementList") and isinstance(v, list):
        e["children"] = [c for c in (_json_element(x) for x in v) if c]
    if kind == "Entity":
        e["children"] = [c for c in (_json_element(x) for x in obj.get("statements") or []) if c]
    return e


def _parse_json(data):
    j = json.loads(data)
    model = {"shells": [], "submodels": []}
    for s in j.get("assetAdministrationShells", []):
        info = s.get("assetInformation") or {}
        model["shells"].append({"idShort": s.get("idShort", ""), "id": s.get("id", ""),
                                "assetKind": info.get("assetKind", ""),
                                "globalAssetId": info.get("globalAssetId", ""),
                                "desc": _lang_json(s.get("description"))})
    for sm in j.get("submodels", []):
        model["submodels"].append({
            "idShort": sm.get("idShort", ""), "id": sm.get("id", ""), "semantic": _semantic_json(sm),
            "desc": _lang_json(sm.get("description")),
            "elements": [c for c in (_json_element(x) for x in sm.get("submodelElements") or []) if c]})
    return model


# ------------------------------------------------------------------ AASX 읽기

def read_model(path):
    """AASX에서 AAS 모델을 읽는다. 실패하면 'error' 키에 이유를 담아 돌려준다."""
    try:
        z = zipfile.ZipFile(path)
    except zipfile.BadZipFile:
        return {"error": "AASX(zip) 파일을 열 수 없음"}
    for name in z.namelist():
        low = name.lower()
        if "_rels" in low or "content_types" in low or "aasx-origin" in low:
            continue
        try:
            if low.endswith(".xml"):
                data = z.read(name)
                if b"assetAdministrationShell" not in data:
                    continue
                m = _parse_xml(data)
            elif low.endswith(".json"):
                data = z.read(name)
                if b"assetAdministrationShells" not in data:
                    continue
                m = _parse_json(data)
            else:
                continue
        except (ET.ParseError, ValueError) as exc:
            return {"error": f"AAS 모델을 읽는 중 오류: {exc}"}
        if m["shells"] or m["submodels"]:
            m["part"] = name
            return m
    return {"error": "AAS 모델을 찾지 못함"}


def read_thumbnail(path):
    """AASX 패키지 관계(_rels/.rels)에 지정된 썸네일 이미지를 (확장자, bytes)로 돌려준다."""
    try:
        z = zipfile.ZipFile(path)
        rels = z.read("_rels/.rels").decode("utf-8", "replace")
    except (zipfile.BadZipFile, KeyError):
        return None
    m = re.search(r'<Relationship[^>]*Type="[^"]*thumbnail"[^>]*Target="([^"]+)"', rels) or \
        re.search(r'<Relationship[^>]*Target="([^"]+)"[^>]*Type="[^"]*thumbnail"', rels)
    if not m:
        return None
    target = posixpath.normpath(m.group(1).lstrip("/"))
    try:
        data = z.read(target)
    except KeyError:
        return None
    ext = posixpath.splitext(target)[1].lower() or ".png"
    return _shrink(ext, data)


def _shrink(ext, data):
    """썸네일을 긴 변 THUMB_PX 이하로 줄인다. Pillow가 없으면 1MB 이하일 때만 원본을 쓴다."""
    try:
        import io
        from PIL import Image
    except ImportError:
        return (ext, data) if len(data) <= 1_000_000 else None
    try:
        img = Image.open(io.BytesIO(data))
        img.thumbnail((THUMB_PX, THUMB_PX))
        out = io.BytesIO()
        if img.mode in ("RGBA", "LA", "P"):
            img.save(out, format="PNG", optimize=True)
            return ".png", out.getvalue()
        img.convert("RGB").save(out, format="JPEG", quality=85, optimize=True)
        return ".jpg", out.getvalue()
    except Exception:  # 손상되었거나 지원하지 않는 이미지
        return None


# ------------------------------------------------------------------ Markdown

def _cell(s, limit=MAX_VALUE):
    s = re.sub(r"\s+", " ", str(s)).strip().replace("|", "\\|")
    return s if len(s) <= limit else s[:limit - 1] + "…"


def _count(elems):
    return sum(1 + _count(e["children"]) for e in elems)


def _rows(elems, depth, out):
    for e in elems:
        pad = "&nbsp;&nbsp;&nbsp;" * depth + ("└ " if depth else "")
        name = f"{pad}**{_cell(e['idShort'], 60)}**" if e["children"] else f"{pad}{_cell(e['idShort'], 60)}"
        sem = f"<sub>{_cell(e['semantic'], 70)}</sub>" if e["semantic"] else ""
        kind = KIND_KO.get(e["kind"], e["kind"])
        if e["children"]:
            kind += f" ({len(e['children'])})"
        kind = kind.replace(" ", "&nbsp;")  # 좁은 화면에서 글자 단위로 줄바꿈되지 않게
        out.append(f"| {name} | {kind} | {_cell(e['value'])} | {sem} |")
        _rows(e["children"], depth + 1, out)


def render(aasx_path, model, *, equipment_readme, aasx_link, thumb_name=None, size_text=""):
    L = [f"# 🧩 {aasx_path.name}", "",
         f"[← 장비 페이지]({equipment_readme}) · [⤓ AASX 다운로드]({aasx_link})" + (f" · {size_text}" if size_text else ""),
         "", "> 🤖 AASX 파일을 열어 자동으로 만든 열람 페이지입니다. 직접 고치지 말고 AASX를 다시 올리세요.", ""]
    if model.get("error"):
        return "\n".join(L + [f"> ⚠️ {model['error']}", ""])

    sms = model["submodels"]
    total = sum(_count(sm["elements"]) for sm in sms)
    if thumb_name:
        L += [f'<img src="{quote(thumb_name)}" alt="썸네일" height="180" align="right">', ""]
    L += ["| 항목 | 내용 |", "|---|---|"]
    for sh in model["shells"][:1]:
        L += [f"| AAS idShort | `{_cell(sh['idShort'])}` |",
              f"| AAS id | <sub>{_cell(sh['id'], 120)}</sub> |",
              f"| 자산 종류 (assetKind) | {_cell(sh['assetKind']) or '-'} |",
              f"| globalAssetId | <sub>{_cell(sh['globalAssetId'], 120) or '-'}</sub> |"]
        if sh["desc"]:
            L.append(f"| 설명 | {_cell(sh['desc'], 200)} |")
    L += [f"| 서브모델 | {len(sms)}개 |", f"| 전체 요소 | {total:,}개 |", ""]

    L += ["## 서브모델 한눈에 보기", "", "| # | 서브모델 | 요소 수 | semanticId |", "|:-:|---|--:|---|"]
    for n, sm in enumerate(sms, 1):
        L.append(f"| {n} | [{_cell(sm['idShort'], 60)}](#sm-{n}) | {_count(sm['elements']):,} | <sub>{_cell(sm['semantic'], 90)}</sub> |")
    L += ["", "## 서브모델 상세", "", "각 서브모델 이름을 누르면 펼쳐집니다. **굵은 글씨**는 하위 요소가 있는 묶음입니다.", ""]

    budget = MAX_ROWS
    for n, sm in enumerate(sms, 1):
        rows = []
        _rows(sm["elements"], 0, rows)
        cut = len(rows) > budget
        shown = rows[:max(budget, 0)]
        budget -= len(shown)
        L += [f'<a id="sm-{n}"></a>', "<details>",
              f"<summary><b>{n}. {_cell(sm['idShort'], 80)}</b> — 요소 {_count(sm['elements']):,}개</summary>", ""]
        if sm["desc"]:
            L += [f"> {_cell(sm['desc'], 300)}", ""]
        if sm["semantic"]:
            L += [f"semanticId: `{_cell(sm['semantic'], 150)}`", ""]
        if shown:
            L += ["| idShort | 종류 | 값 | semanticId |", "|---|---|---|---|", *shown]
        if len(rows) > len(shown):
            L += ["", f"_요소가 많아 일부({len(rows) - len(shown):,}개)는 생략했습니다. 전체 내용은 AASX를 내려받아 AASX Package Explorer로 확인하세요._"]
        L += ["", "</details>", ""]
    return "\n".join(L)
