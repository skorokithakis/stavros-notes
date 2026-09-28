# Wherewhen

**Project:** Travel planner app.

**Repo:** https://github.com/skorokithakis/wherewhen

## Details

Feature ideas are tracked as tickets in the Wherewhen project on Linear. Status follows the general Linear rule (owner, 27 Sep 2026): fully formed, ready-to-build tickets go in Needs Input (the developer agent picks them up); half-formed ideas and notes go in Backlog.

**Agent API:** each trip can be shared with an agent via a per-trip token URL, `https://www.wherewhen.cc/api/agent/<token>/`. GET on the URL returns a Markdown guide with the trip's current JSON at the end. Endpoints: `trip/` (GET, PATCH name/startDate/paddingMin), `places/?q=` (Google Places search, up to 5 candidates), `days/` (POST to append, PATCH/DELETE `days/ID/`), `stops/` (POST place or placeholder, PATCH/DELETE `stops/ID/`, POST `stops/ID/move/`). Days have computed dates and can't be reordered. Ideas list = dayId "ideas". Every write returns the full trip. It can't create, delete or share trips, or return computed schedules or travel times. Tokens for specific trips are kept in scratchpad (Wherewhen agent API tokens), not here.

**Stavrobot plugin (official, installed):** `wherewhen`, written by Stavros, repo https://github.com/stavrobot/plugin-wherewhen (commits 3ed4631, d3821a9, 5a0603e), listed as official in the Stavrobot plugin index. Installed 2026-09-27 14:40, config `trip_token` (full agent URL or bare token) = one trip at a time, currently the "Iceland" trip. Generic: to work on another trip, switch the token (owner rule, never use the raw API). Tools: get_trip, update_trip, search_places, add/update/delete_day, add/update/delete/move_stop. Linear project "Stavrobot Wherewhen plugin" (https://linear.app/stavrosk/project/stavrobot-wherewhen-plugin-d49cab4452da), lead Stavros, Repo link set.

**Old coder-built plugin:** local `wherewhen` (commits 26f4c36, 40a2161, config `agent_token`), never pushed. Removed 2026-09-27 14:40 when the official one was installed.

## Log

- **2026-09-26:** Stavros told me he made Wherewhen, a travel planner. Existing Linear tickets: STA-309 (send reminders for things, Backlog), STA-314 (add calendar functionality, Needs Input). New feature requests go into the Linear Backlog (superseded 27 Sep, see below).
- **2026-09-27:** Stavros shared the agent API for his "Milan" trip (15-22 Oct 2026, 8 days). I read the guide. Read-only review so far, no edits made.
- **2026-09-27:** Stavros asked for a Stavrobot plugin for the agent API. The first two coder attempts failed (coder's Claude Code 2.1.251 was too old for the model). The third succeeded (10 tools, 45 mocked tests). Configured with the "Anyma Athens" trip token (30 Oct start, 1 day, empty), and a read-only get_trip works and survived a Stavrobot restart.
- **2026-09-27 13:46:** At Stavros's request, created the public repo stavrobot/plugin-wherewhen.
- **2026-09-27 13:47:** Stavros said he won't push our coder-built plugin and will write a new one. Created Linear project "Stavrobot Wherewhen plugin" with Repo link to the new repo.
- **2026-09-27 14:39:** Stavros pushed his own plugin (3 commits, 14:34-14:37) and it appears in the official plugin index. At his request I removed the coder-built plugin, installed the official one from the repo, configured it with the Anyma Athens token, and verified get_trip (4 days, 21 ideas).
- **2026-09-27 18:46-18:57:** Stavros shared a third trip, "Iceland" (13-14 Oct, empty). I read it via the raw API and wrongly called the plugin "Anyma only". He clarified the plugin is generic and set the rule: always switch the plugin's trip_token when working on a trip, never use the raw API. Created STA-368 (Needs Input, Agent) in "Stavrobot Wherewhen plugin" to add this guidance to the plugin's manifest instructions (docs only, no code changes).
- **2026-09-27 21:29:** Stavros dropped the "Wherewhen features always go to Backlog" rule. Wherewhen tickets now follow the general Linear rule: ready ones go in Needs Input, half-formed ones in Backlog.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 27, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
