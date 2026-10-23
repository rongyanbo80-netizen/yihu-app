/* sw.js —— 离线缓存：首次加载后断网也能用 */
const CACHE = 'yihu-xiaohu-v1';

const ASSETS = [
  './',
  './index.html',
  './module.html',
  './terminal.html',
  './manifest.json',
  './favicon.png',
  './assets/css/style.css',
  './assets/js/data.js',
  './assets/js/app.js',
  './assets/js/module.js',
  './assets/js/terminal.js',
  './assets/img/logo.svg',
  './assets/icons/icon-192.png',
  './assets/icons/icon-512.png',
  './assets/icons/apple-touch-icon.png'
];

// 九个模块的图标与插画
['fall', 'voice', 'ptz', 'gesture', 'object', 'remote', 'medicine', 'message', 'report'].forEach(function (id) {
  ASSETS.push('./assets/img/icon-' + id + '.svg');
  ASSETS.push('./assets/img/hero-' + id + '.svg');
});

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE).then(function (cache) {
      return cache.addAll(ASSETS);
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.filter(function (k) { return k !== CACHE; })
          .map(function (k) { return caches.delete(k); })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

self.addEventListener('fetch', function (event) {
  const req = event.request;
  if (req.method !== 'GET') return;

  // 终端系统（设备局域网）不走缓存
  if (req.url.indexOf('192.168.') > -1) return;

  event.respondWith(
    caches.match(req).then(function (hit) {
      if (hit) return hit;
      return fetch(req).then(function (res) {
        const copy = res.clone();
        caches.open(CACHE).then(function (cache) { cache.put(req, copy); });
        return res;
      }).catch(function () {
        if (req.mode === 'navigate') return caches.match('./index.html');
        return new Response('', { status: 504, statusText: 'Offline' });
      });
    })
  );
});
