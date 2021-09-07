+++
title = "Transfer config between craft"
weight = 5
sort_by = "weight"
insert_anchor_links = "right"
+++
This is the regex I use with Parachute to transfer between planes only the parameters that are transferrable (ie non-plane-specific):

`^(ACRO_LOCKING|OSD.*|RC[\d_]+.*|FLTMODE.*|FLIGHT_OPTIONS|FS_.*|RTL_CLIMB_MIN|RTL_RADIUS|THR_PASS_STAB|THR_SLEWRATE|THR_SUPP_MAN|TKOFF_ACCEL_CNT|TKOFF_ALT|TKOFF_DIST|TKOFF_THR_DELAY|HOME_RESET_ALT|ALT_HOLD_RTL)$`

This will transfer things like the OSD settings, flight modes, failsafe options, etc etc, but will leave things like PID tuning alone.
Use it to set up a new plane by copying over settings from an older plane.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 07, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
