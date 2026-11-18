# Kartlık – notes for Claude

## Who and what
- Owner: GitHub user `forgotten1432`. Talks to Claude in **Turkish**; reply in Turkish.
- Kartlık is an offline Anki-style flashcard PWA for **iPhone** (Safari → Add to Home Screen), published with GitHub Pages: https://forgotten1432.github.io/githubtest/ . It imports Anki `.apkg` files on the device (sql.js + JSZip). No App Store, no build step.
- Users: the owner (English) and a friend who is a **Uyghur** speaker learning **German**.

## Key code (app.js is one large file)
- APKG import **merges** into existing decks. Cards are matched by note GUID + template ord (`ankiKey`), then by Anki card id, then by front text (deck + text without `.ug` elements). Re-importing an updated deck updates content and **keeps progress**. Never go back to replacing all cards.
- Card CSS from decks is scoped to `#cardFace` (`scopeCSS`); deck CSS must never leak into the app UI.
- Speech: per deck **and card template** front/back language (`settings.deckSpeech`, key `deck\u0001templateName`), guessed automatically on import (`langSignal` / `guessGroupLang`). Back side reads only the part after `<hr id=answer>`.
- Built-in decks: `decks/manifest.json` + `.apkg` files in `decks/`, shown under Desteler → Hazır desteler (Ekle / Güncelle).
- `sw.js`: bump the `CACHE` name and the `app.js?v=` query in both `index.html` and `sw.js` whenever app code changes. `decks/` files are fetched network-first so "Güncelle" gets the new file.

## Built-in decks
- `almanca-temel-2000.apkg` – German, 2002 words (A1–B1), two templates (DE→TR, TR→DE), fields: article, word, type, Turkish, forms (plural / verb forms / comparison), example, hint, **Uyghur**, explanation TR, explanation UG (358 hard words have explanations).
  - Source: `tools/almanca-deck/` → `data/*.txt` (words), `ug/*.txt` (Uyghur, key `word` or `kind:word`), `notes/*.txt` (`key|TR|UG`). Rebuild: `cd tools/almanca-deck && pip install genanki && python3 build.py ../../decks/almanca-temel-2000.apkg`. Note GUIDs are stable, so rebuilt decks update in place.
  - Uyghur translations and explanations were written by Claude and are not checked by a native speaker; the owner forwards corrections from his friend.
- `english-b1-b2.apkg` – the owner's own English B1–B2 deck (711 notes, Uyghur meanings). Its template shows the word twice on the back; that is the deck's design, not a Kartlık bug.

## Working rules
- Test in headless Chrome/Playwright against `python3 -m http.server` before pushing (import, study, re-import keeps progress, settings, speech language via a stubbed `speechSynthesis`).
- Commit straight to `main`; the owner uses a phone and wants changes live.
- The separate English course app lives in `forgotten1432/engbridge`; keep the apps separate.
