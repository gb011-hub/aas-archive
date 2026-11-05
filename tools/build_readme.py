#!/usr/bin/env python3
"""장비 폴더에 올라온 파일만 보고 README(전체 현황표 + 장비별 페이지)를 만든다.

사용법:
    python tools/build_readme.py          # README 생성
    python tools/build_readme.py --check  # 확인 필요 항목만 출력 (있으면 종료 코드 1)
"""
import json
import re
import shutil
import sys
import urllib.request
from urllib.parse import quote

import aasx_view
from archive_lib import DOC_PREFIX, REQUIRED, ROOT, SECTIONS, YOUTUBE_CHANNEL, scan, size

_titles = {}


def youtube_title(url):
    """YouTube oEmbed로 영상 제목을 가져온다 (키 불필요). 네트워크가 막혀 있으면 None."""
    if url not in _titles:
        try:
            q = "https://www.youtube.com/oembed?format=json&url=" + quote(url, safe="")
            with urllib.request.urlopen(q, timeout=8) as r:
                _titles[url] = json.load(r).get("title")
        except Exception:
            _titles[url] = None
    return _titles[url]


def rel(path, base):
    return quote(path.relative_to(base).as_posix())


def en_name(it):
    """AASX 파일 이름에서 영문 장비명을 뽑는다 (예: TextilePrintingMachine_v0.0.1 → TextilePrintingMachine)."""
    if not it["aasx"]:
        return ""
    stem = re.split(r"_[vV]\d", it["aasx"][-1]["file"].stem)[0]
    stem = re.sub(r"_(AAS|ReferenceModel)$", "", stem)
    return stem if re.fullmatch(r"[A-Za-z0-9_]+", stem) else ""


def index_doc(it, sec):
    """표의 문서 칸: 바로 볼 수 있으면 '보기', hwp만 있으면 'PDF 필요', 없으면 빈칸."""
    es = it["entries"][sec]
    if not es:
        return ""
    e = es[0]
    if e["view"]:
        return f"[보기]({rel(e['view'], ROOT)})"
    if e["kind"] == "convertible":
        return "변환 중"
    return "PDF 필요"


def index_aasx(it):
    a = it["aasx"][-1]
    v = it.get("views", {}).get(a["file"])
    return f"[v{a.get('version') or '?'}]({rel(v or a['file'], ROOT)})"


def index_sim(it):
    if it["youtube"]:
        return f"[영상]({it['youtube'][0][1]})"
    fs = it["videos"] or it["files"]["시뮬레이션"]
    return f"[보기]({rel(fs[0], ROOT)})" if fs else ""


def build_index(items):
    on = [i for i in items if i["aasx"]]
    off = [i for i in items if not i["aasx"]]
    full = sum(1 for i in items if i["status"] == "완비")
    warn = [i for i in items if i["issues"]]
    L = [
        "# AAS 참조모델 산출물 아카이브",
        "",
        "장비별 개발계획서 · 가이던스 · AASX · 시뮬레이션을 모은 저장소입니다. 표의 링크를 누르면 바로 열립니다.",
        "",
        "> 이 페이지는 **자동 생성**됩니다. 직접 고치지 말고, 장비 폴더에 파일을 올리기만 하세요. "
        "회의용 **데모 저장소**이며, 파일은 [IODA-Lab/aas-portal-site](https://github.com/IODA-Lab/aas-portal-site)의 실제 파일입니다.",
        "",
        f"**{len(items)}종 중 {len(on)}종 등록** · 필수 문서(계획서 · 가이던스 · AASX) 완비 {full}종 · "
        f"확인 필요 {len(warn)}종 · [시뮬레이션 영상 (YouTube)]({YOUTUBE_CHANNEL})",
        "",
        "| 장비군 | 장비 | AASX | 개발계획서 | 가이던스 | 시뮬레이션 |",
        "|---|---|:-:|:-:|:-:|:-:|",
    ]
    prev = None
    for it in on:
        g = it["group"] if it["group"] != prev else ""
        prev = it["group"]
        en = en_name(it)
        sub = " · ".join(x for x in (en, "확인 필요" if it["issues"] else "") if x)
        name = f"[{it['name']}]({rel(it['dir'], ROOT)})" + (f"<br><sub>{sub}</sub>" if sub else "")
        L.append(f"| {g} | {name} | {index_aasx(it)} | {index_doc(it, '개발계획서')} | "
                 f"{index_doc(it, '가이던스')} | {index_sim(it)} |")
    L += ["", "빈칸은 아직 올라오지 않은 자료입니다. PDF 필요는 hwp만 있어 바로 볼 수 없는 문서입니다.", "", "---", ""]

    L += [f"<details><summary>확인 필요 {len(warn)}종</summary>", "", "| 장비 | 고칠 내용 |", "|---|---|"]
    for it in warn:
        short = [re.sub(r" \(예: [^)]*\)", "", m).replace("|", "/") for m in it["issues"]]
        L.append(f"| [{it['name']}]({rel(it['dir'], ROOT)}) | " + "<br>".join(short) + " |")
    L += ["", "AASX 이름 규칙: `영문장비명_v0.0.1.aasx` (v는 소문자, `_AAS_` 같은 덧붙임 없이)", "", "</details>", ""]

    groups = {}
    for it in off:
        groups.setdefault(it["group"], []).append(f"[{it['name']}]({rel(it['dir'], ROOT)})")
    L += [f"<details><summary>아직 자료가 없는 장비 {len(off)}종</summary>", "", "| 장비군 | 장비 |", "|---|---|"]
    L += [f"| {g} | {', '.join(ns)} |" for g, ns in groups.items()]
    L += ["", "</details>", ""]

    L += [
        "<details><summary>자료 올리는 법</summary>",
        "",
        "1. `equipment/<장비군>/<장비>/` 아래 알맞은 폴더에 원본을 올립니다: "
        "`개발계획서/` · `가이던스/` · `AASX/` · `시뮬레이션/` · `참고자료/`",
        "2. push하면 GitHub Actions가 docx · pptx · xlsx를 PDF로 바꾸고, AASX 열람 페이지와 이 표 · 장비별 페이지를 다시 만듭니다.",
        "",
        "**파일 이름 규칙**",
        "",
        "| 폴더 | 이름 | 예 (장비: PET 사출성형기) |",
        "|---|---|---|",
        f"| `가이던스/` | `{DOC_PREFIX['가이던스']}<장비명>` | `{DOC_PREFIX['가이던스']}PET사출성형기.docx` |",
        f"| `개발계획서/` | `{DOC_PREFIX['개발계획서']}<장비명>` | `{DOC_PREFIX['개발계획서']}PET사출성형기.hwp` + 같은 이름의 `.pdf` |",
        "| `AASX/` | `<영문장비명>_v<버전>.aasx` | `PETInjectionMoldingMachine_v0.0.1.aasx` |",
        "",
        "- 한글(hwp · hwpx)은 자동 변환이 안 되므로 **PDF로 저장해 같은 이름으로 함께** 올립니다.",
        f"- 시뮬레이션 영상은 [YouTube 채널]({YOUTUBE_CHANNEL})에 올리고, 주소를 `시뮬레이션/링크.md`에 적습니다. "
        "표에 '영상'으로 표시되고 누르면 바로 재생됩니다. mp4를 직접 올리면 내려받아야 재생됩니다 (파일당 100MB 제한).",
        "",
        "**자동으로 채워지는 값**",
        "",
        "| 값 | 어디서 가져오나 |",
        "|---|---|",
        "| 장비군 · 장비명 | 폴더 이름 |",
        "| 영문명 · AASX 버전 | AASX 파일 이름 (`영문장비명_v0.0.1`) |",
        "| 보기 링크 | 바로 열리는 PDF · AASX 열람 페이지 · YouTube 주소 |",
        "| 바로 보기용 PDF | docx · pptx · xlsx를 LibreOffice로 자동 변환 |",
        "| AASX 열람 페이지 | AASX를 열어 서브모델 · 요소 · 값 · semanticId를 표로 펼침 (장비 폴더의 `gen/`) |",
        "| 확인 필요 | 파일 이름 규칙, AASX 개수, 내용이 똑같은 중복 파일 |",
        "",
        "</details>",
        "",
    ]
    return "\n".join(L)


def view_cell(e, it):
    d = it["dir"]
    k = e["kind"]
    if e["view"]:
        return f"[보기]({rel(e['view'], d)})"
    if k == "viewable":
        return f"[보기]({rel(e['file'], d)})"
    if k == "video":
        return "다운로드 후 재생"
    if k == "convertible":
        return "PDF 변환 대기"
    if k == "no_preview":
        return "PDF를 함께 올려 주세요"
    if k == "aasx":
        v = it.get("views", {}).get(e["file"])
        return f"[열람 페이지]({rel(v, d)})" if v else "열람 페이지 생성 실패"
    return "다운로드"


def build_equipment(it):
    d = it["dir"]
    L = [
        f"# {it['name']}",
        "",
        f"[전체 목록]({'../' * 3}README.md) · 장비군: **{it['group']}**",
        "",
        "> 자동 생성 페이지입니다. 이 폴더에 파일을 올리면 내용이 갱신됩니다.",
        "",
    ]
    if it.get("thumb"):
        L += [f'<img src="{rel(it["thumb"], d)}" alt="{it["name"]}" height="160" align="right">', ""]
    have = [s for s in REQUIRED if it["files"][s]]
    L += [f"필수 산출물 {len(have)}/{len(REQUIRED)} · " + " · ".join(
        f"{s} {'있음' if it['files'][s] else '없음'}" for s in REQUIRED), ""]
    if it["issues"]:
        L += ["> [!WARNING]", "> **확인 필요**", ">"] + [f"> - {m}" for m in it["issues"]] + [""]

    if it["status"] == "예정":
        L += ["## 산출물", "", "아직 올라온 파일이 없습니다. 아래 폴더에 파일을 올리면 이 페이지가 자동으로 채워집니다.", ""]
        L += [f"- `{s}/`" for s in SECTIONS] + [""]
        return "\n".join(L)

    L += ["## 산출물", "", "| 구분 | 파일 | 크기 | 보기 |", "|---|---|---|---|"]
    for sec in SECTIONS:
        entries = it["entries"][sec]
        if not entries and sec in REQUIRED:
            L.append(f"| {sec} | 아직 없음 | | |")
        for e in entries:
            f = e["file"]
            L.append(f"| {sec} | [{f.name}]({rel(f, d)}) | {size(f.stat().st_size)} | {view_cell(e, it)} |")
    L.append("")

    seen = set()
    for a in it["aasx"]:
        if a["sha1"] in seen:
            continue
        seen.add(a["sha1"])
        subs = a.get("submodels") or []
        view = it.get("views", {}).get(a["file"])
        L += [f"## AAS 구성 — `{a.get('idShort') or '?'}`", "",
              f"`{a['file'].name}` 에서 읽은 서브모델 {len(subs)}개"
              + (f" · **[요소 전체 보기]({rel(view, d)})**" if view else "") + ":", "",
              "| # | 서브모델 idShort |", "|:-:|---|"]
        L += [f"| {n} | {s} |" for n, s in enumerate(subs, 1)] + [""]
    if it["youtube"]:
        L += ["## 시뮬레이션 영상", "", "썸네일을 누르면 YouTube에서 재생됩니다.", ""]
        for vid, url in it["youtube"]:
            title = youtube_title(url) or "YouTube에서 보기"
            L += [f'<a href="{url}"><img src="https://img.youtube.com/vi/{vid}/hqdefault.jpg" '
                  f'alt="{title}" width="360"></a>', "", f"**{title}**", ""]
    if it["uml"]:
        L += ["## 서브모델 설계 (UML)", ""]
        L += [f"- [{f.name}]({rel(f, d)})" for f in it["uml"]] + [""]
    if it.get("history"):
        # 맨 아래 접어 두는 변경 기록 (올림 · 수정 · 삭제). 자동 생성 커밋은 빼고 사람이 한 변경만.
        L += ["<details>", f"<summary>변경 기록 (최근 {len(it['history'])}건)</summary>", "",
              "| 날짜 | 올린 사람 | 내용 |", "|---|---|---|"]
        L += [f"| {d_} | {who} | {msg.replace('|', '/')} |" for d_, who, msg in it["history"]]
        L += ["", "</details>", ""]
    return "\n".join(L)


def build_views(it):
    """장비 폴더의 gen/에 AASX 열람 페이지와 썸네일을 만든다. gen/은 매번 새로 만든다."""
    d = it["dir"]
    gen = d / "gen"
    if gen.exists():
        shutil.rmtree(gen)
    it["views"], it["thumb"] = {}, None
    for a in it["aasx"]:
        f = a["file"]
        gen.mkdir(exist_ok=True)
        thumb_name = None
        t = aasx_view.read_thumbnail(f)
        if t:
            thumb_name = f"{f.stem}_thumbnail{t[0]}"
            (gen / thumb_name).write_bytes(t[1])
            it["thumb"] = it["thumb"] or gen / thumb_name
        model = aasx_view.read_model(f)
        page = gen / f"{f.stem}.md"
        page.write_text(aasx_view.render(
            f, model, equipment_readme="../README.md", aasx_link=quote(f"../{f.relative_to(d).as_posix()}"),
            thumb_name=thumb_name, size_text=size(f.stat().st_size)), encoding="utf-8")
        it["views"][f] = page


def ensure_folders():
    """모든 장비 폴더에 하위 폴더 5개가 보이게 한다. 파일을 다 지워 빈 폴더가 되면 .gitkeep을 다시 넣는다."""
    from archive_lib import EQUIP
    for d in (p for p in EQUIP.glob("*/*") if p.is_dir()):
        for sec in SECTIONS:
            sub = d / sec
            sub.mkdir(exist_ok=True)
            real = [f for f in sub.iterdir() if f.name != ".gitkeep"]
            keep = sub / ".gitkeep"
            if not real and not keep.exists():
                keep.touch()


def main():
    if "--check" not in sys.argv:
        ensure_folders()
    items = scan()
    if "--check" in sys.argv:
        for it in items:
            for m in it["issues"]:
                print(f"⚠️ {it['group']}/{it['name']}: {m}")
        n = sum(len(i["issues"]) for i in items)
        print(f"{len(items)}개 장비, 확인 필요 {n}건")
        sys.exit(1 if n else 0)
    for it in items:
        build_views(it)
    (ROOT / "README.md").write_text(build_index(items), encoding="utf-8")
    for it in items:
        (it["dir"] / "README.md").write_text(build_equipment(it), encoding="utf-8")
    print(f"README 생성: 전체 1개 + 장비 {len(items)}개, AASX 열람 페이지 {sum(len(i['views']) for i in items)}개")


if __name__ == "__main__":
    main()
