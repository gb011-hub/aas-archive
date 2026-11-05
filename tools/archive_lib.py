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

VIEWABLE = {".pdf", ".md", ".txt", ".png", ".jpg", ".jpeg", ".gif", ".svg"}  # GitHub 화면에서 바로 보이는 형식
CONVERTIBLE = {".docx", ".doc", ".pptx", ".xlsx"}                   # LibreOffice로 PDF 자동 변환
NO_PREVIEW_DOC = {".hwp", ".hwpx"}                                    # 자동 변환 불가 → PDF를 함께 올려야 함
VIDEO = {".mp4", ".webm", ".mov"}
LINK_TEXT = {".md", ".txt"}                                           # YouTube 주소를 적는 파일

YOUTUBE_CHANNEL = "https://www.youtube.com/@%ED%95%9C%EC%96%91%EB%8C%80%ED%95%99%EA%B5%90%EC%A0%9C%EC%A1%B0%EB%8D%B0%EC%9D%B4%ED%84%B0"
YOUTUBE_ID = re.compile(
    r"(?:youtube\.com/(?:watch\?(?:[^\s)\]]*&)?v=|shorts/|live/|embed/)|youtu\.be/)([A-Za-z0-9_-]{11})")

# 문서 이름 규칙: <접두어>_<장비명>.<확장자>  (장비명은 폴더 이름, 띄어쓰기는 빼거나 _로 써도 됨)
DOC_PREFIX = {"가이던스": "AAS_활용_가이던스_", "개발계획서": "참조모델_개발계획서_"}


def _norm(s):
    return re.sub(r"[\s_]+", "", s).lower()


def doc_name_ok(section, stem, equipment):
    """문서 파일 이름이 '<접두어>_<장비명>' 규칙을 따르는지. 장비명 뒤에 _v1 같은 덧붙임은 허용."""
    prefix = DOC_PREFIX[section]
    if not stem.startswith(prefix):
        return False
    return _norm(stem[len(prefix):]).startswith(_norm(equipment))


def youtube_links(files):
    """시뮬레이션 폴더의 md/txt 파일에서 YouTube 영상 주소를 찾아 [(영상 ID, 원래 주소)]로 돌려준다."""
    found, seen = [], set()
    for f in files:
        if f.suffix.lower() not in LINK_TEXT:
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in YOUTUBE_ID.finditer(text):
            vid = m.group(1)
            if vid not in seen:
                seen.add(vid)
                found.append((vid, f"https://www.youtube.com/watch?v={vid}"))
    return found


BOT = "github-actions[bot]"
CONVERTED = ROOT / "tools" / "state" / "converted.json"


def git_time(path):
    """파일을 마지막으로 커밋한 시각(유닉스 초). 기록이 없으면 0."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%ct", "--", str(path)],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        return int(out) if out else 0
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return 0


def history(folder, limit=8):
    """장비 폴더의 최근 파일 변경을 [(날짜, 변경, 파일 이름)]으로 돌려준다.
    사람 이름과 커밋 메시지는 쓰지 않고, git 기록의 파일 변경 내역(추가 · 수정 · 삭제 · 이름 변경)만 쓴다.
    자동 생성물(README · gen/ · .gitkeep · 자동 변환 PDF)의 변경과 봇 커밋은 뺀다."""
    r = folder.relative_to(ROOT).as_posix()
    paths = [r, f":(exclude){r}/README.md", f":(exclude){r}/gen", f":(exclude){r}/*/.gitkeep"]
    try:
        out = subprocess.run(["git", "-c", "core.quotepath=off", "log", "-n", "50", "-M", "--name-status",
                              "--format=@@%ad%x1f%an", "--date=short", "--", *paths],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    auto = {p.relative_to(ROOT).as_posix() for p in auto_pdfs()}
    action = {"A": "추가", "M": "수정", "D": "삭제", "R": "이름 변경"}
    commits, cur = [], None
    for line in out.splitlines():
        if line.startswith("@@"):
            date, who = line[2:].split("\x1f", 1)
            cur = {"date": date, "bot": who == BOT, "files": []}
            commits.append(cur)
        elif cur is not None and "\t" in line:
            cur["files"].append(line.split("\t"))
    rows = []
    for c in commits:
        if c["bot"]:
            continue
        # 같은 커밋에 같은 이름의 docx 등이 있으면 그 PDF는 변환본이므로 뺀다
        stems = {f[-1].rsplit(".", 1)[0] for f in c["files"] if f[-1].lower().endswith(tuple(CONVERTIBLE))}
        for parts in c["files"]:
            code, path = parts[0][:1], parts[-1]
            if code not in action or path in auto:
                continue
            if path.lower().endswith(".pdf") and path.rsplit(".", 1)[0] in stems:
                continue
            name = path.rsplit("/", 1)[-1]
            if code == "R":
                name = f"{parts[1].rsplit('/', 1)[-1]} → {name}"
            rows.append((c["date"], action[code], name))
            if len(rows) >= limit:
                return rows
    return rows


def auto_pdfs():
    """자동 변환으로 만든 PDF 경로 집합 (tools/state/converted.json)."""
    try:
        return {ROOT / p for p in json.loads(CONVERTED.read_text(encoding="utf-8"))}
    except (FileNotFoundError, ValueError):
        return set()


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
                it["issues"].append("내용이 완전히 같은 AASX: " + ", ".join(f"`{n}`" for n in names) + ". 하나만 남기세요")
            if not dup:
                it["issues"].append(f"AASX가 {len(it['aasx'])}개 — 최신본 하나만 남기거나 장비를 나누세요")

        auto = auto_pdfs()
        for sec in ("개발계획서", "가이던스"):
            for e in it["entries"][sec]:
                # 사람이 함께 올린 PDF가 원본보다 오래되었으면 (원본만 고치고 PDF는 그대로 둔 경우)
                if e["view"] and e["view"] != e["file"] and e["view"] not in auto \
                        and git_time(e["file"]) > git_time(e["view"]):
                    it["issues"].append(f"`{e['view'].name}`이(가) 원본 `{e['file'].name}`보다 오래되었습니다 "
                                        "— PDF도 다시 저장해 올려 주세요")
        it["history"] = history(d)

        it["no_preview"] = [e["file"] for es in it["entries"].values() for e in es
                            if e["kind"] == "no_preview" and not e["view"]]
        it["videos"] = [e["file"] for e in it["entries"]["시뮬레이션"] if e["kind"] == "video"]
        it["youtube"] = youtube_links(it["files"]["시뮬레이션"])

        for sec, prefix in DOC_PREFIX.items():
            for e in it["entries"][sec]:
                if not doc_name_ok(sec, e["file"].stem, it["name"]):
                    example = f"{prefix}{it['name'].replace(' ', '')}{e['file'].suffix}"
                    it["issues"].append(f"{sec} 파일 이름 규칙 위반: `{e['file'].name}` (예: `{example}`)")
        items.append(it)
    return items


def size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit in ("B", "KB") else f"{n:.1f} {unit}"
        n /= 1024
