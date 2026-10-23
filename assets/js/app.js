/* app.js —— 首页渲染、安装提示与离线注册 */
(function () {
  const grid = document.getElementById('grid');

  MODULES.forEach(function (m) {
    const a = document.createElement('a');
    a.className = 'card';
    a.href = 'module.html?id=' + encodeURIComponent(m.id);
    a.setAttribute('aria-label', m.name + '，查看详情');
    a.innerHTML =
      '<span class="ico" style="background:' + m.tint + '">' +
      '<img src="assets/img/icon-' + m.id + '.svg" alt="" width="34" height="34">' +
      '</span>' +
      '<span>' +
      '<h3>' + m.name + '</h3>' +
      '<p>' + m.short + '</p>' +
      '<span class="go">查看详情 <span aria-hidden="true">›</span></span>' +
      '</span>';
    grid.appendChild(a);
  });

  // 终端地址提示
  const host = (APP.terminalUrl || '').replace(/^https?:\/\//, '').replace(/\/+$/, '');
  const hostEl = document.getElementById('terminal-host');
  if (hostEl && host) hostEl.textContent = host + ' · 需与设备在同一 Wi-Fi';

  const ver = document.getElementById('app-version');
  if (ver) ver.textContent = APP.version;

  // 注册 Service Worker（file:// 打开时自动跳过）
  if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('sw.js').catch(function (err) {
        console.warn('Service Worker 注册失败：', err);
      });
    });
  }

  /* ---------- 安装提示 ---------- */
  const bar = document.getElementById('install-bar');
  const tip = document.getElementById('install-tip');
  const btn = document.getElementById('install-btn');
  const close = document.getElementById('install-close');
  let deferred = null;

  function isStandalone() {
    return window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true;
  }

  function dismissed() {
    try { return localStorage.getItem('yihu-install-dismissed') === '1'; } catch (e) { return false; }
  }

  function show() {
    if (!bar || isStandalone() || dismissed()) return;
    bar.hidden = false;
  }

  function hide(remember) {
    if (bar) bar.hidden = true;
    if (remember) {
      try { localStorage.setItem('yihu-install-dismissed', '1'); } catch (e) {}
    }
  }

  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault();
    deferred = e;
    show();
  });

  window.addEventListener('appinstalled', function () {
    hide(true);
  });

  if (btn) {
    btn.addEventListener('click', function () {
      if (deferred) {
        deferred.prompt();
        deferred.userChoice.then(function () {
          deferred = null;
          hide(false);
        });
      } else {
        hide(true);
      }
    });
  }

  if (close) {
    close.addEventListener('click', function () { hide(true); });
  }

  // iOS Safari 没有安装事件，给出文字指引
  const ua = navigator.userAgent;
  if (/iPad|iPhone|iPod/.test(ua) && !isStandalone() && !dismissed()) {
    if (tip) tip.textContent = '点底部「分享」→「添加到主屏幕」';
    if (btn) btn.textContent = '知道了';
    show();
  }
})();
