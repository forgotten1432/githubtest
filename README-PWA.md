# Kartlık PWA

Turkish offline-first Anki deck reader for iPhone Safari. Import `.apkg` files locally; SQLite, ZIP, Zstandard and media data are processed on-device. No runtime server or account is used.

## GitHub Pages

This repository is configured for static hosting from the root of `main`. Open the GitHub Pages settings and choose `Deploy from a branch` → `main` → `/ (root)` if Pages is not already enabled.

## Install on iPhone

Open the Pages HTTPS URL in Safari once, wait for the app shell to cache, then choose Share → Add to Home Screen. It can then be opened offline. Import `.apkg` through the Data tab.

The app stores decks and media in IndexedDB on this device. It does not sync with AnkiWeb. Keep the original `.apkg` as a backup; CSV export only saves card text.

See `README-PWA.md` for more installation and compatibility notes. Third-party library license notices are in `libs/`.
