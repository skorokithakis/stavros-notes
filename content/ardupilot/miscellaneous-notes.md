+++
title = "Miscellaneous notes"
weight = 4
sort_by = "weight"
insert_anchor_links = "right"
+++
These are random AP-related notes that wouldn't fit anywhere else:

## DJI FPV configuration

If you got some DJI goggles, here's the relevant configuration you need to make:

1. Set `OSD_TYPE=3`.
2. Set `SERIALn_PROTO=33 SERIALn_BAUD=115 SERIALn_OPTIONS=0` (DJI FPV).
3. Create a text file called `naco.txt` on the SD card of the Air Unit with the text `1` in it [to unlock full power](https://oscarliang.com/dji-fpv-system-fcc-700mw/).
4. Create a text file called `naco_pwr.txt` on the SD card of the goggles with the text `pwr_2` in it [to unlock more full power](https://oscarliang.com/dji-fpv-system-1200mw-output/).
5. Set "Custom OSD" to "on" in the goggles menu.
6. Arrange your OSD elements how you like them.

That's it!

* * *

<p style="font-size:80%; font-style: italic">
Last updated on October 19, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
