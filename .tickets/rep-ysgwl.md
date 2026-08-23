---
id: rep-ysgwl
status: closed
deps: [rep-lqvlr]
links: []
created: 2026-08-23T01:00:27Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Remove emoji prefixes from the note tree

Objective: drop the emoji prefixes from every sidebar entry. 71 near-identical document glyphs dominate the sidebar and work against the calm look the restyle is going for. Entries where only some items carry an emoji read as accidental rather than chosen, so remove them for both folders and notes.

joplinexport writes them into the SUMMARY link text:
- Folder.get_summary_line (line ~54) emits the folder's Joplin emoji, or a folder glyph as fallback.
- Note.get_summary_line (line ~106) emits a document glyph unconditionally.

Remove both. mdBook derives <title> from the SUMMARY link text, so this also cleans up browser tab titles, which currently read like '<glyph> A simple guide to PID control - Stavros' Notes'.

Folder.icon then becomes dead: it is read only by that one line. Also remove the field, the 'icon' column from the folders SELECT (line ~209) and the json.loads that decodes it (line ~212). Confirm nothing else reads it before deleting.

Also strip the prefixes from the committed content/SUMMARY.md in the same change, so the built site is correct without a Joplin re-export. Expect the diff to touch all 71 entries. Titles and paths must be otherwise byte-identical; the only change is the removed prefix and the space after it.

joplinexport cannot be run here because it needs a Joplin database. Verify by building and inspecting the rendered sidebar and page titles.

Non-goals: no changes to note content, no changes to slugs or URLs, no other joplinexport behaviour changes.

## Acceptance Criteria

No emoji in the rendered sidebar or in any page's <title>. content/SUMMARY.md differs from the previous version only by removed prefixes. The site builds and every sidebar link still resolves.


## Notes

**2026-08-23T01:00:41Z**

Ready for implementation. Plan approved by Stavros on the Linear ticket (STA-161).
