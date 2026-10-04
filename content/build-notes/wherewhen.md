# Wherewhen

**Project:** Travel planner app.

**Repo:** https://github.com/skorokithakis/wherewhen

## Details

Feature ideas are tracked as tickets in the Wherewhen project on Linear. Status follows the general Linear rule (owner, 27 Sep 2026): fully formed, ready-to-build tickets go in Needs Input (the developer agent picks them up); half-formed ideas and notes go in Backlog. No Agent label on tickets (owner, 30 Sep 2026). Exception: feedback from Petra Vukmirovic (via her Stavrobot Signal agent) always goes to Backlog with a "[Petra] " title prefix (owner, 29 Sep 2026).

**Stack (GitHub languages, 30 Sep 2026):** mostly TypeScript, with a Python backend plus HTML/CSS; Dockerfile and Procfile.

**Agent API:** each trip can be shared with an agent via a per-trip token URL, `https://www.wherewhen.cc/api/agent/<token>/`. GET on the URL returns a Markdown guide with the trip's current JSON at the end. Endpoints: `trip/` (GET, PATCH name/startDate/paddingMin), `places/?q=` (Google Places search, up to 5 candidates), `days/` (POST to append, PATCH/DELETE `days/ID/`), `stops/` (POST place or placeholder, PATCH/DELETE `stops/ID/`, POST `stops/ID/move/`). Days have computed dates and can't be reordered. Ideas list = dayId "ideas". Every write returns the full trip. It can't create, delete or share trips, or return computed schedules or travel times. Tokens for specific trips are kept in scratchpad (Wherewhen agent API tokens), not here.

**Stavrobot plugin (official, installed):** `wherewhen`, written by Stavros, repo https://github.com/stavrobot/plugin-wherewhen (commits 3ed4631, d3821a9, 5a0603e), listed as official in the Stavrobot plugin index. Installed 2026-09-27 14:40, config `trip_token` (full agent URL or bare token) = one trip at a time. Which trip is currently configured is tracked in the scratchpad (Wherewhen tokens), not here. Generic: to work on another trip, switch the token (owner rule, never use the raw API). Tools: get_trip, update_trip, search_places, add/update/delete_day, add/update/delete/move_stop. Linear project "Stavrobot Wherewhen plugin" (https://linear.app/stavrosk/project/stavrobot-wherewhen-plugin-d49cab4452da), lead Stavros, Repo link set.

**Old coder-built plugin:** local `wherewhen` (commits 26f4c36, 40a2161, config `agent_token`), never pushed. Removed 2026-09-27 14:40 when the official one was installed.

### Features as demoed to Petra (29 Sep 2026, from a Gemini summary)
- Reworked main screen and login/account creation (Google sign-in supported). Trips are single-user by default; collaborators are invited by email from trip settings, and the trip appears on their home screen live. Live collaborative editing and offline support.
- Trip creation asks for a date and name before a destination (any placeholder date works if dates aren't known).
- Per-trip agent link/token: paste it into an agent (e.g. Stavrobot on Signal) to generate ideas or arrange unassigned ideas into days. Ideas carry Google Maps links, addresses, ratings and reviews. Direct in-app chat is planned.
- Drag-and-drop ideas into days; pinned durations (e.g. one hour for a meal) stay fixed when the schedule shifts; pinned end times.
- Calendar subscription link for all trip events. Day view for use during the trip: live overview, departure warnings, transit time to the next stop.
- Transit mode per leg (drive, walk, cycle). Travel events (flights/trains between airports) draw a transit line on the schedule.
- Hotels are ordinary stops, not a special entity: duplicate the hotel as the first/last stop of each day and pin end times to constrain the day. Chosen for flexibility (e.g. multi-day cruise boats).
- Invite-code system to keep it free for friends without abuse; users can generate their own invite codes in account settings.
- Mobile: tapping items zooms/pans the map.
- Plans: Stavros intends to charge eventually because LLM usage will be costly. Not open source: he wants only his agents to open pull requests, no outside contributors.

### In-app LLM chat (30 Sep 2026) - now Linear STA-427 (first spike, In Progress)
The original design ticket STA-423 was later marked Done and then trashed with the other Done tickets on 30 Sep. Current work: STA-427 "Task: in-app LLM trip assistant chat, first spike", In Progress, assigned to Stavros.
Stavros wants a chat in Wherewhen that helps plan trips, can search the web and makes other tool calls. He said it needs extensive design before building. Advice given (not decisions): no full agent harness needed. Use the plain Anthropic SDK (Python or TypeScript) with a simple tool loop: call the model, and on `stop_reason == tool_use` run the tool, append a tool_result and repeat until `end_turn`. Web search via Anthropic's server-side `web_search` tool (plus optional `web_fetch`), which runs inside the API request with citations, needs no search key and is billed per search; handle `pause_turn`. App tools mirror the agent API (search_places, add_stop, move_stop...). Stream to the frontend via SSE. Open design questions (from the original ticket): scope tools to the current trip server-side (the model never passes trip ids); web content can carry prompt injection while the chat has write access, so make writes undoable or confirm them first; cost caps vs invite codes/paid tiers; chat placement in the UI; what trip context is sent; model choice.

### Feature request from Keigo Suzukawa (30 Sep 2026, from a Gemini summary of a work 1:1) - undecided
- Pain point: organising family trips across several countries (Australia, France and Poland mentioned) is high-friction.
- Suggested: shared to-dos, a status dashboard for trip tasks (e.g. "flights booked?"), and travel concierge integrations.
- Stavros's reservations: travel styles differ widely (minute-by-minute planning vs all-inclusive vs sightseeing maps), and task tracking risks turning the app into a Jira-like tracker. He acknowledged shared to-dos/tracking as a possible idea; target niche and implementation not decided. Not filed in Linear.

### Stavros's feedback session (3-4 Oct 2026)
Eight points, all filed at his request as Linear tickets in Wherewhen, Backlog, no labels: STA-494 to STA-501. Full wording, my (unconfirmed) readings and open questions are in [Wherewhen feedback - 3 Oct 2026](/build-notes/wherewhen-feedback-3-oct-2026.html).

## Log

- **2026-09-26:** Stavros told me he made Wherewhen, a travel planner. Existing Linear tickets: STA-309 (send reminders for things, Backlog), STA-314 (add calendar functionality, Needs Input). New feature requests go into the Linear Backlog (superseded 27 Sep, see below).
- **2026-09-27:** Stavros shared the agent API for his "Milan" trip (15-22 Oct 2026, 8 days). I read the guide. Read-only review so far, no edits made.
- **2026-09-27:** Stavros asked for a Stavrobot plugin for the agent API. The first two coder attempts failed (coder's Claude Code 2.1.251 was too old for the model). The third succeeded (10 tools, 45 mocked tests). Configured with the "Anyma Athens" trip token (30 Oct start, 1 day, empty), and a read-only get_trip works and survived a Stavrobot restart.
- **2026-09-27 13:46:** At Stavros's request, created the public repo stavrobot/plugin-wherewhen.
- **2026-09-27 13:47:** Stavros said he won't push our coder-built plugin and will write a new one. Created Linear project "Stavrobot Wherewhen plugin" with Repo link to the new repo.
- **2026-09-27 14:39:** Stavros pushed his own plugin (3 commits, 14:34-14:37) and it appears in the official plugin index. At his request I removed the coder-built plugin, installed the official one from the repo, configured it with the Anyma Athens token, and verified get_trip (4 days, 21 ideas).
- **2026-09-27 18:46-18:57:** Stavros shared a third trip, "Iceland" (13-14 Oct, empty). I read it via the raw API and wrongly called the plugin "Anyma only". He clarified the plugin is generic and set the rule: always switch the plugin's trip_token when working on a trip, never use the raw API. Created STA-368 (Agent) in "Stavrobot Wherewhen plugin" to add this guidance to the plugin's manifest instructions (docs only, no code changes). STA-368 was Done as of 30 Sep.
- **2026-09-27 21:29:** Stavros dropped the "Wherewhen features always go to Backlog" rule. Wherewhen tickets now follow the general Linear rule: ready ones go in Needs Input, half-formed ones in Backlog.
- **2026-09-29 15:23:** Demo call with Petra Vukmirovic (source: Gemini summary, not a transcript). Petra had been confused on her first try; Stavros showed the reworked login and main screen, invited her to a trip by email, and walked through agent ideas, scheduling, pinning, calendar subscription, day view, hotels and travel events (details above). Petra's feedback: what to do when dates aren't known yet (workaround: placeholder date); **bug: the map shows Greece regardless of destination until a place is added**; selecting schedule items/highlighting on the map is janky (Stavros acknowledged); earlier trouble on mobile (Stavros showed recent fixes); suggested basing recommendations on where the hotel is over time; proposed voting on ideas. **Voting: undecided** - Petra prefers 1-5 stars, Stavros leaned towards thumbs up/down reactions in each user's colour. Next steps from the summary for Stavros: add a settings icon to the trip header (committed in the call); open GitHub issues to Petra (later in the call the Signal bot -> Linear route was set up instead); reaction system for ideas (summary lists it, but the decision is still open); restrict Linear so members only see specific projects (Petra could see all projects; both worried about permissions and prompt injection since LLMs process tickets). Petra: test with a Portugal trip; invite her sister to test for her Croatia trip; report feedback from 'Aroena' (unidentified). They also debated AI's effect on engineering hiring: Petra thinks language fluency matters less than domain knowledge and critical thinking; Stavros thinks the bar has risen and mid-skill developers without specialisms are left behind.
- **2026-09-29 15:44:** Laid out the Las Vegas trip's ideas over days 1-2 (Bellagio as start stop each day, per the hotel-as-stop pattern).
- **2026-09-29 16:00-16:22:** Set up a Stavrobot Signal agent (agent 26) for Petra's Wherewhen feedback. Her items reach the main agent and are filed as "[Petra] " tickets in the Wherewhen project Backlog; the agent itself has no Linear access.
- **2026-09-29 22:40:** Filled the "barca's" (Barcelona, 6-8 Oct) trip with sample stops at his request (18 stops + 1 idea).
- **2026-09-30 00:15:** Added 50 region-tagged ideas to a second "Iceland" trip (10-13 Oct 2027, 4 days) at his request; days left empty.
- **2026-09-30 00:21 (Pebble):** Asked whether in-app LLM chat with web search and tool calls needs a full harness or just a library (Python?). Advised plain SDK + tool loop + Anthropic server-side web search (see "In-app LLM chat" above).
- **2026-09-30 00:25:** At his request, filed STA-423 "In-app LLM chat for trip planning (needs design)" in Wherewhen, Backlog (verified with get_issue). He noted it needs extensive design first.
- **2026-09-30 00:26:** Stavros said tickets never need the Agent label any more. Removed it from STA-423 (now no labels, still Backlog); rule updated in the Linear scratchpad.
- **2026-09-30 (later that night):** STA-423 marked Done; STA-427 "Task: in-app LLM trip assistant chat, first spike" is In Progress, assigned to Stavros. 03:05-03:13: all Done/Canceled Linear tickets (including STA-423) moved to Linear's trash at his request; STA-427 is the only open ticket left.
- **2026-09-30 13:29:** Keigo Suzukawa (Numan colleague) pitched a feature request during a work 1:1 (source: Gemini summary): shared to-dos, trip task status dashboard, concierge integrations. Undecided, see section above.
- **2026-10-03 23:08 - 2026-10-04 01:11:** Feedback session from Stavros (Signal, then Pebble after midnight). At 23:12 he asked for every point to become a Backlog ticket (no labels): STA-494 show ratings on places in the chat; STA-495 ask for the number of days when creating a trip; STA-496 LLM proposes an itinerary the first time a trip switches to itinerary mode; STA-497 teach the LLM Wherewhen best practices (e.g. hotel as first/last stop each day); STA-498 Wikipedia/OpenStreetMap links for places; STA-499 "I'm leaving now" button in the Today view for when you're late; STA-500 rename Ideas mode to Research mode (API dayId "ideas" should stay or be aliased); STA-501 keep the LLM provider abstraction encapsulated (assumed to be Wherewhen, unconfirmed). Collected in [Wherewhen feedback - 3 Oct 2026](/build-notes/wherewhen-feedback-3-oct-2026.html).

* * *

<p style="font-size:80%; font-style: italic">
Last updated on October 04, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
