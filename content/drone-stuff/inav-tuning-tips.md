+++
title = "INAV tuning tips"
weight = 3
sort_by = "weight"
insert_anchor_links = "right"
+++
Here are some general INAV tuning tips and things I've learned throughout my builds. Keep in mind that *these only apply to wings* (and maybe planes), not quads:

* There's a known problem with horizon drift. To ameliorate it, use `set imu_acc_ignore_rate = 10`.
* To make turns in automatic turns smoother, use `set nav_fw_control_smoothness = 8`.
* Pawel says that the idea of the software LPF is to replace the hardware LPF. Leave the hardware LPF set to 256 Hz and set the software LPF to 20-30 Hz, with a looptime of 1k.

* * *

*Last updated on November 30, 2020.*
