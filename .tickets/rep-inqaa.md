---
id: rep-inqaa
status: closed
deps: [rep-vfwmk]
links: []
created: 2026-08-23T01:00:16Z
type: task
priority: 1
assignee: Stavros Korokithakis
---
# Restyle the site: rewrite static/custom.css

Objective: replace the current 3-line static/custom.css with a real stylesheet. Target look is a personal notes site, not product documentation: warm off-white background, Source Serif 4 body and headings, narrower measure, generous space around headings.

Scope: static/custom.css (full rewrite) and one line in book.toml. Nothing else.

TWO LOOKS ACROSS FIVE THEME CLASSES
mdBook puts one of light/rust/coal/navy/ayu on <html>. Put the light palette on 'html' unconditionally and the dark palette on 'html.coal, html.navy, html.ayu'. That yields exactly two deliberate looks, needs less CSS than styling five, and makes an unstyled state unreachable for a visitor whose localStorage holds an old theme choice.
Set preferred-dark-theme = "coal" in book.toml [output.html]. Hide the theme picker (#mdbook-theme-toggle).

PREFER OVERRIDING mdBook's CSS CUSTOM PROPERTIES over fighting its rules. The full set is in mdBook's css/variables.css; it includes --bg, --fg, --sidebar-bg, --sidebar-fg, --sidebar-active, --sidebar-spacer, --links, --inline-code-color, --quote-bg, --quote-border, --table-border-color, --table-header-bg, --table-alternate-bg, --blockquote-{note,tip,important,warning,caution}-color, --content-max-width, --mono-font, --icons, --icons-hover, the --search* family, --footnote-highlight and --overlay-bg.

LAYOUT
- Measure down to roughly 680px.
- Let pre and .table-wrapper extend wider than the text column (around 760px) so long code lines and tables are not cramped.
- Hide the floating gutter nav (.nav-wide-wrapper) and always show the bottom nav (.nav-wrapper). The nav anchors are icon-only in mdBook's markup with no chapter title available; do not try to add titles.

TYPOGRAPHY
- Build a real hierarchy between h1/h2/h3 and body text. Currently they differ mostly in weight.
- mdBook sets root font-size to 62.5%, so 1rem = 10px. Work with that, do not fight it.
- mdBook's general.css already applies 'h2, h3 { margin-block-start: 2.5em }'. The old custom.css overrode this to 1.5em; decide deliberately what the new value should be rather than carrying it over by habit.

SIDEBAR
Give the 71-entry tree real hierarchy: section entries visually distinct from leaf entries, an indent guide for children, and a clear active item.
CONSTRAINT: the sidebar renders inside an iframe (toc.html, injected by toc.js). custom.css IS loaded in that document so styling works, but no selector can span the parent document and the sidebar. Verified against the live site.

ALSO STYLE
Links, inline code, code blocks, tables, blockquotes, the GitHub-style admonitions, hr, images (constrain max-width), and task-list checkboxes (./build makes them interactive on purpose, so keep them usable).

Do not regress print.html, which ./build post-processes.

Around 200-250 lines is the expected size. Not a hard limit.

Non-goals: no theme/ directory or Handlebars template override, no JavaScript, no edits to mdBook's own CSS files, no search UI redesign, no note content changes.

## Design

A template override would give full control but makes every future mdBook upgrade a merge. mdBook 0.5.2 exposes enough CSS custom properties to do this from custom.css alone, so upgrades stay routine. That constraint is deliberate.

Mapping five theme classes onto two palettes was chosen over styling two classes and hiding the rest, because hiding the picker would otherwise leave returning visitors stranded in an unstyled palette held in localStorage.

## Acceptance Criteria

Previewed through .symphony/serve at both desktop and mobile widths, in light and dark, on the index page, a page with code blocks, and a page with a table: the site looks deliberate and consistent, and no mdBook UI element (search, sidebar, menu bar, admonitions) is left visibly unstyled or broken.


## Notes

**2026-08-23T01:00:41Z**

Ready for implementation. Plan approved by Stavros on the Linear ticket (STA-161).
