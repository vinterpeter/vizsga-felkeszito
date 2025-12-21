// Service Worker for Vizsgafelkeszito PWA
const CACHE_VERSION = '1.3.2';
const CACHE_NAME = `vizsga-cache-v${CACHE_VERSION}`;
const DATA_CACHE_NAME = `vizsga-data-v${CACHE_VERSION}`;
const MEDIA_CACHE_NAME = `vizsga-media-v${CACHE_VERSION}`;

// Core files that are always cached
const CORE_FILES = [
    './',
    './index.html',
    './index_EREDETI.html',
    './manifest.json',
    './icon-192.png',
    './icon-512.png'
];

// External CDN resources
const CDN_FILES = [
    'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.1',
    'https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js',
    'https://cdn.jsdelivr.net/npm/marked/marked.min.js'
];

// Media directories (chapters)
const CHAPTERS = ['02', '03', '04', '05', '06', '07', '08'];

// Install event - cache core files
self.addEventListener('install', (event) => {
    console.log('[SW] Installing service worker...');
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('[SW] Caching core files');
                return cache.addAll(CORE_FILES);
            })
            .then(() => {
                self.skipWaiting();
            })
    );
});

// Activate event - clean old caches
self.addEventListener('activate', (event) => {
    console.log('[SW] Activating service worker...');
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    // Delete old versioned caches
                    if (cacheName.startsWith('vizsga-') &&
                        cacheName !== CACHE_NAME &&
                        cacheName !== DATA_CACHE_NAME &&
                        cacheName !== MEDIA_CACHE_NAME) {
                        console.log('[SW] Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => {
            return self.clients.claim();
        })
    );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);

    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }

    // Handle media files (larger files)
    if (url.pathname.includes('/media/')) {
        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                if (cachedResponse) {
                    return cachedResponse;
                }
                return fetch(event.request).then((response) => {
                    // Don't cache if not successful
                    if (!response || response.status !== 200) {
                        return response;
                    }
                    // Clone and cache
                    const responseToCache = response.clone();
                    caches.open(MEDIA_CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                    return response;
                }).catch(() => {
                    // Return offline placeholder for media if not cached
                    return new Response('Offline - media not available', {
                        status: 503,
                        statusText: 'Service Unavailable'
                    });
                });
            })
        );
        return;
    }

    // Handle CDN resources
    if (url.hostname !== location.hostname) {
        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                if (cachedResponse) {
                    return cachedResponse;
                }
                return fetch(event.request).then((response) => {
                    if (!response || response.status !== 200) {
                        return response;
                    }
                    const responseToCache = response.clone();
                    caches.open(DATA_CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                    return response;
                });
            })
        );
        return;
    }

    // Handle core app files - network first, fallback to cache
    event.respondWith(
        fetch(event.request)
            .then((response) => {
                if (!response || response.status !== 200) {
                    return caches.match(event.request);
                }
                const responseToCache = response.clone();
                caches.open(CACHE_NAME).then((cache) => {
                    cache.put(event.request, responseToCache);
                });
                return response;
            })
            .catch(() => {
                return caches.match(event.request);
            })
    );
});

// Message handler for manual caching operations
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'CACHE_URLS') {
        const urls = event.data.urls;
        const cacheName = event.data.cacheName || MEDIA_CACHE_NAME;

        event.waitUntil(
            caches.open(cacheName).then(async (cache) => {
                let completed = 0;
                const total = urls.length;

                for (const url of urls) {
                    try {
                        const response = await fetch(url);
                        if (response.ok) {
                            await cache.put(url, response);
                        }
                        completed++;
                        // Report progress
                        self.clients.matchAll().then((clients) => {
                            clients.forEach((client) => {
                                client.postMessage({
                                    type: 'CACHE_PROGRESS',
                                    completed,
                                    total,
                                    url
                                });
                            });
                        });
                    } catch (error) {
                        console.error('[SW] Failed to cache:', url, error);
                        completed++;
                    }
                }

                // Report completion
                self.clients.matchAll().then((clients) => {
                    clients.forEach((client) => {
                        client.postMessage({
                            type: 'CACHE_COMPLETE',
                            total: completed
                        });
                    });
                });
            })
        );
    }

    if (event.data && event.data.type === 'GET_CACHE_SIZE') {
        event.waitUntil(
            getCacheSize().then((size) => {
                event.source.postMessage({
                    type: 'CACHE_SIZE',
                    size
                });
            })
        );
    }

    if (event.data && event.data.type === 'CLEAR_CACHE') {
        event.waitUntil(
            Promise.all([
                caches.delete(CACHE_NAME),
                caches.delete(DATA_CACHE_NAME),
                caches.delete(MEDIA_CACHE_NAME)
            ]).then(() => {
                event.source.postMessage({
                    type: 'CACHE_CLEARED'
                });
            })
        );
    }

    if (event.data && event.data.type === 'GET_VERSION') {
        event.source.postMessage({
            type: 'VERSION',
            version: CACHE_VERSION
        });
    }
});

// Helper function to get total cache size
async function getCacheSize() {
    let totalSize = 0;
    const cacheNames = await caches.keys();

    for (const cacheName of cacheNames) {
        if (cacheName.startsWith('vizsga-')) {
            const cache = await caches.open(cacheName);
            const keys = await cache.keys();

            for (const request of keys) {
                const response = await cache.match(request);
                if (response) {
                    const blob = await response.clone().blob();
                    totalSize += blob.size;
                }
            }
        }
    }

    return totalSize;
}
