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
from archive_lib import REQUIRED, ROOT, SECTIONS, scan, size

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


REPO = "https://github.com/gb011-hub/aas-archive"


def inquiry_url(name):
    """장비명이 미리 채워진 문의 양식 (IODA-Lab과 같은 .github/ISSUE_TEMPLATE/equipment-question.yml)."""
    from urllib.parse import urlencode
    q = urlencode({"template": "equipment-question.yml", "title": f"[문의] {name}", "equipment": name})
    return f"{REPO}/issues/new?{q}"


def build_manage(items):
    """equipment/README.md: 확인 필요 목록과 자료 올리는 법 (첫 화면은 IODA 방식으로 깔끔하게 두고 여기에 모은다)."""
    warn = [i for i in items if i["issues"]]
    L = [
        "# 자료 관리",
        "",
        "[전체 목록](../README.md)",
        "",
        "> 자동 생성 페이지입니다. 장비 폴더에 파일을 올리거나 고치거나 지우면 PDF 변환 · AASX 열람 페이지 · "
        "장비별 페이지 · 이 목록이 자동으로 갱신됩니다.",
        "",
        f"## 확인 필요 ({len(warn)}종)",
        "",
    ]
    if warn:
        L += ["| 장비 | 고칠 내용 |", "|---|---|"]
        for it in warn:
            short = [m.replace("|", "/") for m in it["issues"]]
            L.append(f"| [{it['name']}]({rel(it['dir'], ROOT / 'equipment')}) | " + "<br>".join(short) + " |")
    else:
        L.append("없음")
    L += [
        "",
        "## 자료 올리는 법",
        "",
        "1. 장비 폴더 `equipment/<장비군>/<장비>/` 아래 알맞은 폴더에 원본을 올립니다: "
        "`개발계획서/` · `가이던스/` · `AASX/` · `시뮬레이션/` · `참고자료/`",
        "2. GitHub Actions가 PDF 변환 · AASX 열람 페이지 · 장비별 페이지 · 첫 화면을 자동으로 다시 만듭니다 (1 ~ 3분).",
        "",
        "### 파일 이름 규칙 (IODA-Lab/aas-portal-site와 같음)",
        "",
        "| 폴더 | 이름 | 예 (장비: PET 사출성형기) |",
        "|---|---|---|",
        "| `개발계획서/` | `<장비명>_개발계획서` | `PET사출성형기_개발계획서.hwp` |",
        "| `가이던스/` | `<장비명>_가이던스` | `PET사출성형기_가이던스.docx` |",
        "| `AASX/` | `<영문장비명>_v<버전>.aasx` | `PETInjectionMoldingMachine_v0.0.1.aasx` |",
        "",
        "- 장비명은 폴더 이름에서 띄어쓰기 · 가운뎃점 · 괄호 부분을 뺀 것입니다. 예: `디스크 탈수기(DISCFILTER)` → `디스크탈수기`",
        "- hwp · docx는 자동으로 PDF가 만들어집니다. hwpx는 PDF를 같은 이름으로 함께 올립니다.",
        "- 시뮬레이션 영상은 YouTube에 올리고 `tools/archive-index/videos.csv`에 장비 · 주소 · 길이를 한 줄 적습니다 "
        "(zip · mp4는 올리지 않습니다).",
        "- 장비 담당자는 `tools/archive-index/authors.csv`, 담당자 GitHub 계정은 `owner_accounts.csv`에 적습니다. "
        "첫 화면의 담당자 이름을 누르면 문의 양식이 열리고, 등록된 문의는 담당자에게 자동으로 지정됩니다.",
        "- 웹 업로드는 파일당 25MB까지입니다. 더 큰 파일은 GitHub Desktop으로 올립니다 (100MB까지).",
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
        f"[전체 목록]({'../' * 3}README.md) · 장비군: **{it['group']}** · [이 장비 문의하기]({inquiry_url(it['name'])})",
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
            length = it.get("youtube_len", {}).get(url)
            title += f" ({length})" if length else ""
            L += [f'<a href="{url}"><img src="https://img.youtube.com/vi/{vid}/hqdefault.jpg" '
                  f'alt="{title}" width="360"></a>', "", f"**{title}**", ""]
    if it["uml"]:
        L += ["## 서브모델 설계 (UML)", ""]
        L += [f"- [{f.name}]({rel(f, d)})" for f in it["uml"]] + [""]
    if it.get("history"):
        # 맨 아래 접어 두는 변경 기록 (올림 · 수정 · 삭제). 자동 생성 커밋은 빼고 사람이 한 변경만.
        L += ["<details>", f"<summary>변경 기록 (최근 {len(it['history'])}건)</summary>", "",
              "| 날짜 | 변경 | 파일 |", "|---|---|---|"]
        L += [f"| {d_} | {act} | {name.replace('|', '/')} |" for d_, act, name in it["history"]]
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
    # 첫 화면(README.md)은 tools/archive-index/build_index.py(IODA-Lab 방식)가 만든다
    (ROOT / "equipment" / "README.md").write_text(build_manage(items), encoding="utf-8")
    for it in items:
        (it["dir"] / "README.md").write_text(build_equipment(it), encoding="utf-8")
    print(f"README 생성: 자료 관리 1개 + 장비 {len(items)}개, AASX 열람 페이지 {sum(len(i['views']) for i in items)}개")


if __name__ == "__main__":
    main()
