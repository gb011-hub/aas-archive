// hwp5html 결과(HTML)를 Chrome으로 A4 인쇄하기 전에 실행하는 스크립트.
// 1) 페이지 폭을 넘는 표는 페이지 폭으로 다시 배치 (칸 너비 자동, 긴 글자는 줄바꿈)
// 2) 그래도 넘치는 표만 따로 축소 (최소 60%)
// GitHub Actions(hwp-test 브랜치)에서 개발계획서 4종으로 시험해 잘림이 없는 것을 확인함.
(function () {
  var avail = 718;  // A4 본문 폭 190mm (좌우 여백 10mm)
  // 1) 넘치는 표는 페이지 폭으로 다시 배치
  var tables = document.querySelectorAll('table'), fixed = 0, zoomed = 0, minz = 1;
  for (var i = 0; i < tables.length; i++) {
    var t = tables[i];
    if (t.getBoundingClientRect().right <= avail) continue;
    t.style.width = '100%'; t.style.maxWidth = '100%'; t.style.tableLayout = 'auto';
    var cells = t.querySelectorAll('td,th,col');
    for (var j = 0; j < cells.length; j++) { cells[j].style.width = 'auto'; cells[j].style.wordBreak = 'break-all'; }
    fixed++;
  }
  // 2) 그래도 넘치는 표만 따로 축소 (최소 60%)
  for (var i = 0; i < tables.length; i++) {
    var t = tables[i], r = t.getBoundingClientRect();
    if (r.right <= avail || t.parentElement.closest('table')) continue;
    var z = Math.max(0.6, (avail - r.left) / r.width);
    t.style.zoom = z; zoomed++; if (z < minz) minz = z;
  }
})();
