#!/usr/bin/env python3
"""docx · pptx · xlsx를 바로 보기용 PDF로 변환하고, 원본이 바뀌거나 지워지면 PDF도 따라가게 한다.

자동 변환한 PDF는 tools/state/converted.json에 "어느 원본의 어떤 내용(해시)으로 만들었는지" 기록한다.
  - 원본이 새로 올라옴          → PDF 생성
  - 원본 내용이 바뀜 (같은 이름) → PDF 다시 생성
  - 원본이 삭제되거나 이름이 바뀜 → 예전 PDF 삭제
  - 사람이 직접 올린 PDF        → 기록에 없으므로 건드리지 않음 (자동 변환보다 우선)

사용법:
    python tools/convert_docs.py          # 변환 · 정리 실행 (LibreOffice 필요)
    python tools/convert_docs.py --plan   # 변환이 필요한 파일 수만 출력 (LibreOffice 설치 여부 판단용)
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EQUIP = ROOT / "equipment"
STATE = ROOT / "tools" / "state" / "converted.json"
SOURCES = {".docx", ".doc", ".pptx", ".xlsx"}


def sha1(path):
    return hashlib.sha1(path.read_bytes()).hexdigest()


def rel(path):
    return path.relative_to(ROOT).as_posix()


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8")), False
    # 기록이 처음 생기는 경우: 원본과 같은 이름의 PDF는 지금까지 규칙상 자동 변환본이므로 그대로 등록
    state = {}
    for src in sorted(EQUIP.rglob("*")):
        if src.suffix.lower() in SOURCES and src.with_suffix(".pdf").exists():
            state[rel(src.with_suffix(".pdf"))] = {"source": rel(src), "sha1": sha1(src)}
    return state, True


def plan(state):
    """(변환할 원본 목록, 지울 PDF 목록)"""
    todo = []
    for src in sorted(EQUIP.rglob("*")):
        if src.suffix.lower() not in SOURCES or not src.is_file():
            continue
        pdf = src.with_suffix(".pdf")
        rec = state.get(rel(pdf))
        if pdf.exists() and rec is None:
            continue                        # 사람이 올린 PDF가 있음
        if not pdf.exists() or rec["source"] != rel(src) or rec["sha1"] != sha1(src):
            todo.append(src)
    orphans = [p for p, rec in state.items() if not (ROOT / rec["source"]).exists()]
    return todo, orphans


def main():
    state, created = load_state()
    todo, orphans = plan(state)
    if "--plan" in sys.argv:
        print(len(todo))
        return
    for p in orphans:
        (ROOT / p).unlink(missing_ok=True)
        del state[p]
        print(f"원본이 없어 PDF 삭제: {p}")
    for src in todo:
        print(f"PDF 변환: {rel(src)}")
        r = subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(src.parent), str(src)],
                           capture_output=True, text=True)
        pdf = src.with_suffix(".pdf")
        if r.returncode == 0 and pdf.exists():
            state[rel(pdf)] = {"source": rel(src), "sha1": sha1(src)}
        else:
            print(f"  ⚠️ 변환 실패: {rel(src)}")
    if todo or orphans or created:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(json.dumps(dict(sorted(state.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"변환 {len(todo)}개, 삭제 {len(orphans)}개" + (" (변환 기록 새로 만듦)" if created else ""))


if __name__ == "__main__":
    main()
