+++
title = "Miscellaneous"
weight = 8
sort_by = "weight"
insert_anchor_links = "right"
+++
This is a bunch of miscellaneous info that wouldn't fit anywhere else:

- The ZOHD Dart 250g with the stock motor draws 4.5A on 2S with the 5x5 propeller. It draws the same amperage at exactly 75% throttle with a 3S battery and the same propeller.
- When wiring your electronics, make sure you don't have any ground loops.
  This means that there should only be one ground wire going to each component.
  For example, the ESC has one ground wire for power (to the battery) and one for signal (to the FC), you should *only* use one of the two (the one going to the battery).
  What you can do for the other ground wire, though, is twist it around the signal wire and only connect it to the FC side, to reduce emissions.
  If you have coaxial cable, you can do the same, connect the outer shielding to the FC's ground, and don't connect the other side anywhere, and use the core as signal.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on March 06, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
