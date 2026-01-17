const CACHE_NAME = 'bible-reading-v2';
const urlsToCache = [
  '/BibleReading/',
  '/BibleReading/index.html',
  '/BibleReading/manifest.json',
  '/BibleReading/icon-192.png',
  '/BibleReading/icon-512.png',
  '/BibleReading/plans/mcheyne.json',
  '/BibleReading/plans/oneyearchronological.json',
  '/BibleReading/plans/esvthroughthebible.json',
  '/BibleReading/plans/esvliterarystudybible.json',
  '/BibleReading/plans/heartlightotandnt.json',
  '/BibleReading/plans/fiveday2026.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(cacheName => cacheName !== CACHE_NAME)
          .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
