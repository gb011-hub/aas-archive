"""장비 폴더를 읽어 장비별 정보를 만든다 (README 생성기가 사용).

사람이 따로 적어 넣는 파일은 없다. 모든 값은 폴더 이름, 파일, AASX 내용, git 기록에서 가져온다.
파이썬 표준 라이브러리만 사용한다.
"""
import hashlib
import json
import re
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EQUIP = ROOT / "equipment"

SECTIONS = ["개발계획서", "가이던스", "AASX", "시뮬레이션", "참고자료"]
REQUIRED = ["개발계획서", "가이던스", "AASX"]
ICON = {"개발계획서": "📄", "가이던스": "📘", "AASX": "🧩", "시뮬레이션": "🎬", "참고자료": "🔗"}
STATUS_ICON = {"예정": "⚪", "작성 중": "🟡", "완비": "🟢"}

AASX_NAME = re.compile(r"^[A-Z][A-Za-z0-9]*_v\d+\.\d+\.\d+(_\d{6})?\.aasx$")
VERSION = re.compile(r"_v(\d+\.\d+\.\d+)", re.I)
IGNORE = {".gitkeep", ".DS_Store", "README.md", "index.html"}

VIEWABLE = {".pdf", ".md", ".png", ".jpg", ".jpeg", ".gif", ".svg"}  # GitHub 화면에서 바로 보이는 형식
CONVERTIBLE = {".docx", ".doc", ".pptx", ".xlsx"}                   # LibreOffice로 PDF 자동 변환
NO_PREVIEW_DOC = {".hwp", ".hwpx"}                                    # 자동 변환 불가 → PDF를 함께 올려야 함
VIDEO = {".mp4", ".webm", ".mov"}


def git_last(files):
    """올라온 파일(README·자동 변환 PDF 제외)을 마지막으로 커밋한 사람과 날짜."""
    if not files:
        return None, None
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%an|%ad", "--date=short", "--", *map(str, files)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None, None
    return tuple(out.split("|", 1)) if out else (None, None)


def read_aasx(path):
    info = {"idShort": None, "submodels": []}
    try:
        z = zipfile.ZipFile(path)
    except zipfile.BadZipFile:
        info["error"] = "AASX(zip) 파일을 열 수 없음"
        return info
    for name in z.namelist():
        low = name.lower()
        if "_rels" in low or "content_types" in low or "aasx-origin" in low:
            continue
        if low.endswith(".xml"):
            data = z.read(name).decode("utf-8", "replace")
            shell = re.search(r"<(?:\w+:)?assetAdministrationShell>.*?<(?:\w+:)?idShort>([^<]+)<", data, re.S)
            if not shell:
                continue
            info["idShort"] = shell.group(1)
            info["submodels"] = re.findall(
                r"<(?:\w+:)?submodel>\s*(?:<(?:\w+:)?extensions>.*?</(?:\w+:)?extensions>\s*)?"
                r"<(?:\w+:)?idShort>([^<]+)<", data, re.S)
            return info
        if low.endswith(".json"):
            try:
                j = json.loads(z.read(name))
            except ValueError:
                continue
            if isinstance(j, dict) and j.get("assetAdministrationShells"):
                info["idShort"] = j["assetAdministrationShells"][0].get("idShort")
                info["submodels"] = [s.get("idShort") for s in j.get("submodels", [])]
                return info
    info["error"] = "AAS 모델을 찾지 못함"
    return info


def sha1(path):
    return hashlib.sha1(path.read_bytes()).hexdigest()


def doc_entries(files):
    """문서 목록을 '원본 + 바로 보기용 PDF' 묶음으로 정리한다.
    docx 옆에 같은 이름의 PDF가 있으면 그 PDF는 자동 변환본으로 보고 따로 표시하지 않는다."""
    by_stem = {}
    for f in files:
        by_stem.setdefault(f.stem, []).append(f)
    entries = []
    for stem, group in by_stem.items():
        pdf = next((f for f in group if f.suffix.lower() == ".pdf"), None)
        originals = [f for f in group if f.suffix.lower() != ".pdf"]
        if originals:
            for o in originals:
                entries.append({"file": o, "view": pdf, "kind": kind_of(o)})
        else:
            entries.append({"file": pdf, "view": pdf, "kind": "pdf"})
    return sorted(entries, key=lambda e: e["file"].name)


def kind_of(f):
    ext = f.suffix.lower()
    if ext == ".aasx":
        return "aasx"
    if ext in VIDEO:
        return "video"
    if ext in VIEWABLE:
        return "viewable"
    if ext in CONVERTIBLE:
        return "convertible"
    if ext in NO_PREVIEW_DOC:
        return "no_preview"
    return "other"


def scan():
    items = []
    for d in sorted(p for p in EQUIP.glob("*/*") if p.is_dir()):
        it = {"group": d.parent.name, "name": d.name, "dir": d, "files": {}, "entries": {}, "issues": []}
        for sec in SECTIONS:
            sub = d / sec
            files = sorted(f for f in sub.rglob("*") if f.is_file() and f.name not in IGNORE) if sub.is_dir() else []
            it["files"][sec] = files
            it["entries"][sec] = doc_entries([f for f in files if f.parent == sub])
        uploaded = [e["file"] for es in it["entries"].values() for e in es]
        uploaded += [f for f in it["files"]["AASX"] if f.parent != d / "AASX"]  # AASX/UML 등 하위 폴더
        it["author"], it["updated"] = git_last(uploaded)

        it["aasx"] = []
        for f in it["files"]["AASX"]:
            if f.suffix.lower() != ".aasx":
                continue
            a = read_aasx(f)
            v = VERSION.search(f.name)
            a.update(file=f, version=v.group(1) if v else None, sha1=sha1(f))
            it["aasx"].append(a)
        it["uml"] = [f for f in it["files"]["AASX"] if f.suffix.lower() == ".puml"]

        have = sum(1 for s in REQUIRED if it["files"][s])
        it["status"] = "예정" if not any(it["files"].values()) else ("완비" if have == len(REQUIRED) else "작성 중")

        for a in it["aasx"]:
            if not AASX_NAME.match(a["file"].name):
                it["issues"].append(f"AASX 파일 이름 규칙 위반: `{a['file'].name}` (예: `AirDryer_v0.0.1.aasx`)")
            if a.get("error"):
                it["issues"].append(f"`{a['file'].name}`: {a['error']}")
        if len(it["aasx"]) > 1:
            groups = {}
            for a in it["aasx"]:
                groups.setdefault(a["sha1"], []).append(a["file"].name)
            dup = [n for n in groups.values() if len(n) > 1]
            for names in dup:
                it["issues"].append("내용이 완전히 같은 AASX: " + ", ".join(f"`{n}`" for n in names) + " → 하나만 남기세요")
            if not dup:
                it["issues"].append(f"AASX가 {len(it['aasx'])}개 — 최신본 하나만 남기거나 장비를 나누세요")

        it["no_preview"] = [e["file"] for es in it["entries"].values() for e in es
                            if e["kind"] == "no_preview" and not e["view"]]
        it["videos"] = [e["file"] for e in it["entries"]["시뮬레이션"] if e["kind"] == "video"]
        items.append(it)
    return items


def size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit in ("B", "KB") else f"{n:.1f} {unit}"
        n /= 1024
