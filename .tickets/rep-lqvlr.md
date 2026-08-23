---
id: rep-lqvlr
status: closed
deps: []
links: []
created: 2026-08-23T00:59:45Z
type: chore
priority: 1
assignee: Stavros Korokithakis
---
# Add build/preview scripts and ignore downloaded mdBook artifacts

Objective: make the site buildable and previewable without Joplin access, so theme work can be verified visually.

No fixtures needed. All 71 notes and content/SUMMARY.md are already committed. joplinexport is only required to REGENERATE content from a Joplin database; ./build works from what is in the repo.

Add .symphony/setup (executable):
- Ensure the mdBook v0.5.2 binary is available on PATH. ./build already contains a pinned download fallback; reuse that approach rather than inventing a second one.
- Nothing else to install. scripts/mdbook-linkify.py and move_html_to_dir are pure Python 3 stdlib.

Add .symphony/serve (executable):
- Run: ./build && python3 -m http.server --directory public "${PORT:-8000}"
- Do NOT use 'mdbook serve'. It stops after mdBook and skips the post-processing in ./build: the 'cp -R static/*' that places non-mdBook assets, the sed path rewrites, and move_html_to_dir (page.html -> page/index.html). Those steps finalise asset paths and are where path bugs appear.
- public/ must be served at the server root. Generated HTML uses root-absolute paths (/css/..., path_to_root = ""), so a subpath mount breaks the site.

.gitignore: add the mdbook binary and mdbook.tgz. When mdBook is absent, ./build downloads both into the repo root, and update.sh runs a blind 'git add .'. Verified neither is tracked nor present anywhere in history, so this is preventative only.

Non-goals: no live reload, no change to ./build itself beyond nothing, no CI config.

## Acceptance Criteria

./.symphony/setup then ./.symphony/serve produces a browsable site at the chosen port, with working CSS, fonts and images, and note pages reachable at directory URLs such as /drone-stuff/a-simple-guide-to-pid-control/.


## Notes

**2026-08-23T01:00:41Z**

Ready for implementation. Plan approved by Stavros on the Linear ticket (STA-161).
