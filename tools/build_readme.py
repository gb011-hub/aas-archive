#!/usr/bin/env python3
"""장비 폴더에 올라온 파일만 보고 README(전체 현황표 + 장비별 페이지)를 만든다.

사용법:
    python tools/build_readme.py          # README 생성
    python tools/build_readme.py --check  # 확인 필요 항목만 출력 (있으면 종료 코드 1)
"""
import json
import shutil
import sys
import urllib.request
from urllib.parse import quote

import aasx_view
from archive_lib import (DOC_PREFIX, ICON, REQUIRED, ROOT, SECTIONS, STATUS_ICON, YOUTUBE_CHANNEL,
                         scan, size)

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


def status(it):
    return f"{STATUS_ICON[it['status']]} {it['status']}"


def build_index(items):
    counts = {k: sum(1 for i in items if i["status"] == k) for k in STATUS_ICON}
    warn = sum(1 for i in items if i["issues"])
    nopv = sum(len(i["no_preview"]) for i in items)
    L = [
        "# AAS 참조모델 산출물 아카이브",
        "",
        "> 🤖 이 페이지는 **자동 생성**됩니다. 직접 고치지 말고, 장비 폴더에 파일을 올리기만 하세요.",
        "> 회의용 **데모 저장소**입니다. 들어 있는 파일은 모두 "
        "[IODA-Lab/aas-portal-site](https://github.com/IODA-Lab/aas-portal-site)의 실제 파일입니다 "
        "(AASX 49개, 원본 PDF · 영상 · 참고자료, 스트레쳐 개발계획서 · 가이던스).",
        "",
        f"📺 시뮬레이션 영상: [한양대학교 제조데이터 YouTube 채널]({YOUTUBE_CHANNEL})",
        "",
    ]
    L += [
        "**진행 현황** · " + " · ".join(f"{STATUS_ICON[k]} {k} {counts[k]}" for k in STATUS_ICON)
        + f" · ⚠️ 확인 필요 {warn} · 전체 {len(items)}종",
        "",
        "| 장비군 | 장비 | 상태 | 계획서 | 가이던스 | AASX | 시뮬레이션 | AASX 버전 | 서브모델 | 최근 올린 사람 | 수정일 |",
        "|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|---|---|",
    ]
    prev = None
    for it in items:
        a = it["aasx"][0] if it["aasx"] else {}
        g = f"**{it['group']}**" if it["group"] != prev else ""
        prev = it["group"]
        name = f"[{it['name']}]({rel(it['dir'], ROOT)})" + (" ⚠️" if it["issues"] else "")
        def mark(s):
            if s == "시뮬레이션":
                return "▶️" if it["youtube"] else ("🎬" if it["videos"] else ("✅" if it["files"][s] else "—"))
            return "✅" if it["files"][s] else "—"
        marks = " | ".join(mark(s) for s in ["개발계획서", "가이던스", "AASX", "시뮬레이션"])
        L.append(
            f"| {g} | {name} | {status(it)} | {marks} | {a.get('version') or '-'} "
            f"| {len(a.get('submodels') or []) or '-'} | {it['author'] or '-'} | {it['updated'] or '-'} |"
        )
    L += ["", "## ⚠️ 확인 필요", ""]
    issues = [(it, m) for it in items for m in it["issues"]]
    L += [f"- **{it['group']} / {it['name']}** — {m}" for it, m in issues] or ["- 없음"]
    if nopv:
        L += ["", f"> ℹ️ hwp · hwpx 문서 {nopv}개는 브라우저에서 바로 볼 수 없습니다. "
                  "한글에서 **PDF로 저장해 같은 폴더에 함께 올리면** 자동으로 '바로 보기'가 연결됩니다."]
    L += [
        "",
        "## 사용 방법",
        "",
        "1. `equipment/<장비군>/<장비>/` 아래 알맞은 폴더에 파일을 올립니다: "
        "`개발계획서/` · `가이던스/` · `AASX/` · `시뮬레이션/` · `참고자료/`",
        "2. 끝입니다. push하면 GitHub Actions가 docx를 PDF로 바꾸고, AASX 열람 페이지와 이 표 · 장비별 페이지를 다시 만듭니다.",
        "",
        "### 파일 이름 규칙",
        "",
        "| 폴더 | 이름 | 예 (장비: PET 사출성형기) |",
        "|---|---|---|",
        f"| `가이던스/` | `{DOC_PREFIX['가이던스']}<장비명>` | `{DOC_PREFIX['가이던스']}PET사출성형기.docx` |",
        f"| `개발계획서/` | `{DOC_PREFIX['개발계획서']}<장비명>` | `{DOC_PREFIX['개발계획서']}PET사출성형기.hwp` + 같은 이름의 `.pdf` |",
        "| `AASX/` | `<영문장비명>_v<버전>.aasx` | `PETInjectionMoldingMachine_v0.0.1.aasx` |",
        "",
        "- 장비명은 폴더 이름과 같게 씁니다. 띄어쓰기는 빼거나 `_`로 써도 됩니다.",
        "- 한글(hwp · hwpx)은 브라우저에서 바로 볼 수 없으므로 **PDF로 저장해 같은 이름으로 함께** 올려 주세요.",
        "",
        "### 시뮬레이션 영상",
        "",
        f"- 영상은 [YouTube 채널]({YOUTUBE_CHANNEL})에 올리고, 영상 주소를 적은 텍스트 파일(`.txt` 또는 `.md`)을 "
        "장비의 `시뮬레이션/` 폴더에 올립니다. 장비 페이지에 썸네일이 표시되고, 누르면 YouTube에서 재생됩니다.",
        "- 주소 형식은 `https://youtu.be/…` · `https://www.youtube.com/watch?v=…` 모두 됩니다. 한 파일에 여러 개를 적어도 됩니다.",
        "- mp4를 직접 올려도 보관은 되지만 다운로드해야 재생됩니다 (파일당 100MB 제한).",
        "",
        "| 자동으로 채워지는 값 | 어디서 가져오나 |",
        "|---|---|",
        "| 장비군 · 장비명 | 폴더 이름 |",
        "| 상태 | 산출물 3종(개발계획서 · 가이던스 · AASX) 중 몇 개가 올라왔는지 |",
        "| AASX 버전 | 파일명의 `_v0.0.1` 부분 |",
        "| idShort · 서브모델 목록 | AASX 파일을 직접 열어서 읽음 |",
        "| 최근 올린 사람 · 수정일 | git 커밋 기록 (자동 생성 파일 제외) |",
        "| 바로 보기용 PDF | docx · pptx · xlsx를 LibreOffice로 자동 변환 |",
        "| AASX 열람 페이지 | AASX를 열어 서브모델 · 요소 · 값 · semanticId를 표로 펼침 (장비 폴더의 `gen/`) |",
        "| YouTube 썸네일 · 제목 | `시뮬레이션/` 폴더의 텍스트 파일에 적힌 YouTube 주소 |",
        "| 확인 필요 | 파일 이름 규칙, AASX 개수, 내용이 똑같은 중복 파일 |",
        "",
    ]
    return "\n".join(L)


def view_cell(e, it):
    d = it["dir"]
    k = e["kind"]
    if e["view"]:
        return f"[👁 바로 보기]({rel(e['view'], d)})"
    if k == "viewable":
        return f"[👁 바로 보기]({rel(e['file'], d)})"
    if k == "video":
        return "다운로드 후 재생"
    if k == "convertible":
        return "⏳ PDF 변환 대기"
    if k == "no_preview":
        return "❌ PDF를 함께 올려 주세요"
    if k == "aasx":
        v = it.get("views", {}).get(e["file"])
        return f"[👁 열람 페이지]({rel(v, d)})" if v else "열람 페이지 생성 실패"
    return "다운로드"


def build_equipment(it):
    d = it["dir"]
    L = [
        f"# {it['name']}",
        "",
        f"[← 전체 목록]({'../' * 3}README.md) · 장비군: **{it['group']}**",
        "",
        "> 🤖 자동 생성 페이지입니다. 이 폴더에 파일을 올리면 내용이 갱신됩니다.",
        "",
    ]
    if it.get("thumb"):
        L += [f'<img src="{rel(it["thumb"], d)}" alt="{it["name"]}" height="160" align="right">', ""]
    L += [
        "| 항목 | 내용 |",
        "|---|---|",
        f"| 상태 | {status(it)} |",
        f"| 최근 올린 사람 | {it['author'] or '-'} |",
        f"| 수정일 | {it['updated'] or '-'} |",
        "",
    ]
    if it["issues"]:
        L += ["> [!WARNING]", "> **확인 필요**", ">"] + [f"> - {m}" for m in it["issues"]] + [""]

    if it["status"] == "예정":
        L += ["## 산출물", "", "아직 올라온 파일이 없습니다. 아래 폴더에 파일을 올리면 이 페이지가 자동으로 채워집니다.", ""]
        L += [f"- `{s}/`" for s in SECTIONS] + [""]
        return "\n".join(L)

    L += ["## 산출물", "", "| 구분 | 파일 | 크기 | 바로 보기 |", "|---|---|---|---|"]
    for sec in SECTIONS:
        entries = it["entries"][sec]
        if not entries and sec in REQUIRED:
            L.append(f"| {ICON[sec]} {sec} | _아직 없음_ | | |")
        for e in entries:
            f = e["file"]
            L.append(f"| {ICON[sec]} {sec} | [{f.name}]({rel(f, d)}) | {size(f.stat().st_size)} | {view_cell(e, it)} |")
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
              + (f" · **[👁 요소 전체 펼쳐 보기]({rel(view, d)})**" if view else "") + ":", "",
              "| # | 서브모델 idShort |", "|:-:|---|"]
        L += [f"| {n} | {s} |" for n, s in enumerate(subs, 1)] + [""]
    if it["youtube"]:
        L += ["## ▶️ 시뮬레이션 영상", "", "썸네일을 누르면 YouTube에서 재생됩니다.", ""]
        for vid, url in it["youtube"]:
            title = youtube_title(url) or "YouTube에서 보기"
            L += [f'<a href="{url}"><img src="https://img.youtube.com/vi/{vid}/hqdefault.jpg" '
                  f'alt="{title}" width="360"></a>', "", f"**{title}**", ""]
    if it["uml"]:
        L += ["## 서브모델 설계 (UML)", ""]
        L += [f"- [{f.name}]({rel(f, d)})" for f in it["uml"]] + [""]
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


def main():
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
