+++
title = "INAV tuning tips"
weight = 3
sort_by = "weight"
insert_anchor_links = "right"
+++
Here are some general INAV tuning tips and things I've learned throughout my builds. Keep in mind that *these only apply to wings* (and maybe planes), not quads:

* There's a known problem with horizon drift. To ameliorate it, use `set imu_acc_ignore_rate = 10`. Setting this low is a good idea, but if it's set too low then the accelerometer will effectively be ignored and the horizon will eventually drift. To reduce the accelerometer's influence, you can also reduce `imu_dcm_ki`/`imu_dcm_kp`.
* To make turns in automatic modes smoother, use `set nav_fw_control_smoothness = 8`.
* Pawel says that the idea of the software LPF is to replace the hardware LPF. Leave the hardware LPF set to 256 Hz and set the software LPF to 20-30 Hz, with a looptime of 1k.

* * *

*Last updated on December 15, 2020.*
