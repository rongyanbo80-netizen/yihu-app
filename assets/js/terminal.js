/* terminal.js —— 应用内加载树莓派 Web 控制台 */
(function () {
  const params = new URLSearchParams(location.search);
  const url = params.get('url') ? decodeURIComponent(params.get('url')) : APP.terminalUrl;

  const frame = document.getElementById('frame');
  const fallback = document.getElementById('fallback');
  const tip = document.getElementById('tip');

  document.getElementById('url').textContent = url;
  document.getElementById('fallback-url').textContent = url;
  document.getElementById('open-browser').href = url;
  document.getElementById('external').href = url;

  let settled = false;
  let timer = null;

  function showFallback() {
    if (settled) return;
    settled = true;
    fallback.classList.add('show');
    tip.textContent = '连接超时 · 可尝试用浏览器打开';
  }

  function load() {
    settled = false;
    fallback.classList.remove('show');
    tip.textContent = '正在连接设备…';
    frame.src = url;
    if (timer) clearTimeout(timer);
    // 跨域 iframe 无法直接判断内容，用超时兜底提示
    timer = setTimeout(showFallback, 9000);
  }

  frame.addEventListener('load', function () {
    if (settled) return;
    tip.textContent = '已连接 · 若画面空白请点右上角用浏览器打开';
    if (timer) clearTimeout(timer);
  });

  document.getElementById('retry').addEventListener('click', load);

  document.getElementById('reload').addEventListener('click', function () {
    load();
  });

  document.getElementById('copy-url').addEventListener('click', function () {
    const done = function () {
      tip.textContent = '地址已复制，可粘贴到浏览器打开';
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(done, function () {
        window.prompt('复制下面的地址：', url);
      });
    } else {
      window.prompt('复制下面的地址：', url);
    }
  });

  document.getElementById('back').addEventListener('click', function () {
    if (history.length > 1) history.back();
    else location.href = 'index.html';
  });

  load();
})();
