---
id: rep-vfwmk
status: closed
deps: [rep-lqvlr]
links: []
created: 2026-08-23T00:59:55Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Self-host Source Serif 4 webfont

Objective: add the body/heading typeface the new theme needs.

Add static/fonts/ containing Source Serif 4, latin + latin-ext only (there is no Greek or Cyrillic in the content). Either three static cuts (400, 400 italic, 600) or two variable files (roman + italic), whichever gives the smaller total. Keep the total under roughly 150KB. Source from the adobe-fonts/source-serif releases or Google Fonts. Include the OFL license text alongside the files, since the licence requires it.

Put the @font-face rules in static/custom.css. Do not add a second stylesheet.

CRITICAL - asset URLs must be root-absolute (/fonts/xyz.woff2). move_html_to_dir rewrites page.html to page/index.html, so page depth varies and relative URLs break on nested pages. ./build copies static/* into public/, so static/fonts/x.woff2 is served at /fonts/x.woff2.

mdBook already writes its own hash-named fonts into public/fonts/. The 'cp -R static/*' merges ours alongside them. There are no name collisions, but do not imitate mdBook's hashed naming.

Use font-display: swap.

Leave mdBook's bundled Open Sans and Source Code Pro alone. Browsers only fetch @font-face rules that are actually used, so the unused Open Sans files cost nothing.

Non-goals: no replacement mono font (Source Code Pro is already bundled and stays), no additional weights beyond what the stylesheet uses, no Greek or Cyrillic subsets.

## Acceptance Criteria

Fonts load with no 404s when previewed through .symphony/serve, including on a nested note page, and the served HTML is unaffected.


## Notes

**2026-08-23T01:00:41Z**

Ready for implementation. Plan approved by Stavros on the Linear ticket (STA-161).
