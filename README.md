# PlayBack – Instrumental Adventiste By Sitraka Nambinintsoa

## Fametrahana (indray mandeha ihany)
1. Alefaso eo amin'ny repo `sitraka0417-cell/PlayBack` ny votoatin'ity zip ity (index.html, build_site.py, icon.svg, manifest.webmanifest, robots.txt, .github/…) eo akaikin'ireo dossiers mp3.
2. GitHub → **Settings → Pages → Build and deployment → Source : GitHub Actions**.
3. Andraso ny Action « Mise à jour du site PlayBack » (tab Actions) hifarana. Ny site : https://sitraka0417-cell.github.io/PlayBack/

## Mise à jour auto
Isaky ny `git push` (hira na artiste vaovao = dossier vaovao), mandeha ho azy ny Action : mamaky ny dossiers, mamorona `songs.json`, ary mamoaka ny site.

## Google « Playback Sitraka »
1. Ao amin'ny https://search.google.com/search-console , ampio ny propriété `https://sitraka0417-cell.github.io/PlayBack/` (méthode « Préfixe d'URL »).
2. Ny code fanamarinana dia apetraka ao amin'ny `index.html` (meta google-site-verification, efa misy ny toerana).
3. « Inspection de l'URL » → « Demander une indexation » ary alefaso ny `sitemap.xml`.
