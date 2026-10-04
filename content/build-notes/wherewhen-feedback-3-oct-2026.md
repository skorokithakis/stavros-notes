# Wherewhen feedback - 3 Oct 2026

**Project:** Feedback points on Wherewhen from Stavros, session of 3 Oct 2026 (23:08 onwards, via Signal; points 5-8 via Pebble after midnight). Parent build note: [Wherewhen](/build-notes/wherewhen.html).

At 23:12 Stavros asked for each point to be filed as a Linear ticket in the Wherewhen project, Backlog, no labels.

## Feedback

1. **Add ratings to chat places** (23:09) - [STA-494](https://linear.app/stavrosk/issue/STA-494/show-ratings-on-places-in-the-chat). Places that come up in the chat should show their rating. My reading, unconfirmed: the in-app LLM trip assistant chat ([STA-427](https://linear.app/stavrosk/issue/STA-427)) should display the Google rating (and probably review count) for any place it suggests, the same way ideas already carry ratings and reviews.
2. **Ask for the number of days when creating a trip** (23:09) - [STA-495](https://linear.app/stavrosk/issue/STA-495/ask-for-the-number-of-days-when-creating-a-trip). The trip creation flow currently asks for a date and a name; it should also ask how many days the trip lasts. My reading, unconfirmed: the trip is then created with that many days already in place, instead of being added one at a time afterwards.
3. **LLM proposes a plan the first time you switch to itinerary mode** (23:10) - [STA-496](https://linear.app/stavrosk/issue/STA-496/llm-proposes-an-itinerary-the-first-time-a-trip-switches-to-itinerary). The first time a user switches a trip to itinerary mode, the LLM should plan a recommended itinerary. My reading, unconfirmed: it arranges the collected ideas into the trip's days as a suggested starting schedule, which the user can then edit. Open questions: does it apply automatically or show a proposal to accept or reject, and what happens if the days already have stops? Related to the in-app chat work (STA-427).
4. **Teach the LLM the app's best practices** (23:22) - [STA-497](https://linear.app/stavrosk/issue/STA-497/teach-the-llm-wherewhen-planning-best-practices). Tell the LLM how Wherewhen is meant to be used, e.g. the hotel is duplicated as the first (morning) and last (night) stop of each day. My reading, unconfirmed: a best-practices section in the in-app assistant's system prompt, and probably in the agent API guide too, so external agents follow the same conventions. Other candidates: pinned meal durations, pinned end times to constrain a day, travel events for flights and trains.
5. **Links to Wikipedia / OpenStreetMap for places** (4 Oct 00:27, Pebble) - [STA-498](https://linear.app/stavrosk/issue/STA-498/add-links-to-wikipedia-openstreetmap-for-places). Add links to Wikipedia or OpenStreetMap "or something". My reading, unconfirmed: alongside the existing Google Maps link on stops and ideas, link the place's Wikipedia article (where one exists) and/or OSM page. Open questions: which sources, how to match the right article reliably, and showing links only where a match exists.
6. **Today view: "I'm leaving now" button for when you're late** (4 Oct 00:30, Pebble) - [STA-499](https://linear.app/stavrosk/issue/STA-499/today-view-im-leaving-now-button-for-when-youre-late). In the Today view, offer "I'm leaving now" instead of "I've left" when you're late. My reading, unconfirmed: when behind schedule, the button re-anchors the rest of the day to the current time rather than the planned departure. Open questions: replace "I've left" only when late or show both, what counts as late, and how pinned times interact with the shift.
7. **Rename Ideas mode to Research mode** (4 Oct 00:31, Pebble) - [STA-500](https://linear.app/stavrosk/issue/STA-500/rename-ideas-mode-to-research-mode). Open question: UI label only, or the agent API too (dayId "ideas")? Renaming the API value would break the Stavrobot wherewhen plugin and other agents unless the old name is kept as an alias.
8. **Keep the LLM provider abstraction well encapsulated** (4 Oct 01:11, Pebble) - [STA-501](https://linear.app/stavrosk/issue/STA-501/keep-the-llm-provider-abstraction-well-encapsulated). "Ensure that our LLM provider abstraction is sufficiently encapsulated." Assumed to be Wherewhen (unconfirmed). My reading: all LLM calls go through one provider layer so switching between Anthropic, DeepSeek, Z.ai/GLM or Ollama Cloud is an adapter/config change; watch for provider-specific features (Anthropic server-side web search, pause_turn, prompt caching), streaming and tool-call formats, and per-provider cost accounting. Context: the 3 Oct DeepSeek/GLM price comparison.


* * *

<p style="font-size:80%; font-style: italic">
Last updated on October 04, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
