#!/usr/bin/env bash
# equipment/ 아래 docx·pptx·xlsx 중 같은 이름의 PDF가 없는 파일을 PDF로 변환한다.
# 변환본은 원본 옆에 같은 이름으로 저장된다 (예: 가이던스/X.docx → 가이던스/X.pdf).
# hwp·hwpx는 LibreOffice가 열지 못하므로 변환하지 않는다 (README에 'PDF를 함께 올려 주세요'로 표시).
set -euo pipefail
cd "$(dirname "$0")/.."

converted=0
while IFS= read -r -d '' f; do
  pdf="${f%.*}.pdf"
  [ -e "$pdf" ] && continue
  echo "PDF 변환: $f"
  soffice --headless --convert-to pdf --outdir "$(dirname "$f")" "$f" >/dev/null 2>&1 \
    || echo "  ⚠️ 변환 실패: $f"
  converted=$((converted + 1))
done < <(find equipment -type f \( -iname '*.docx' -o -iname '*.doc' -o -iname '*.pptx' -o -iname '*.xlsx' \) -print0)
echo "변환 대상 ${converted}개 처리"
