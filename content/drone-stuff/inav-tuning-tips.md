+++
title = "INAV tuning tips"
weight = 5
sort_by = "weight"
insert_anchor_links = "right"
+++
Here are some general INAV tuning tips and things I've learned throughout my builds. Keep in mind that *these only apply to wings* (and maybe planes), not quads:

* To make turns in automatic modes smoother, use `set nav_fw_control_smoothness = 8`.
* Pawel says that the idea of the software LPF is to replace the hardware LPF. Leave the hardware LPF set to 256 Hz and set the software LPF to 20-30 Hz, with a looptime of 1k.


## Battery monitoring

To monitor how much battery you have left in flight, voltage isn't a good indication because it can sag a lot. mAh is also not a good indication, because it doesn't decrease linearly with voltage (when voltage drops, you need to consume more amps for the same amount of motor RPM, and thus thrust). Remaining energy (in Watt-hours) is a better way, using the "Wh drawn" INAV OSD item. In addition, INAV has heat loss compensation for the energy meter (done by simulating the internal resistance of the battery), which gives you a more accurate reading.

To calculate the Wh a battery can give, the best way is to charge or discharge it and see how many Wh were spent, if your charger shows you. Another way is to get a rough estimate using the formula `no_cells * 3.7 * Ah`. So, for a 1800 4S battery, the maximum Watt-hours are `4 * 3.7 * 1.8 = 26.64 Wh`. You should not discharge more than 80% of that value, or you risk excessive wear to the battery.

For a 4S battery, I go with a rule of thumb: The maximum Wh is `mAh / 85`, so for a 5000 mAh battery I'll land after 58 Wh consumed, which is around 80% of the battery consumed and gives a small margin for error.

More details can be found in the [battery page](https://notes.stavros.io/drone-stuff/inav-tuning-tips/#battery-monitoring) in the INAV wiki.

_(Thanks to Michel Pastor in the INAV Telegram group for this tip.)_


## Horizon drift issues

There's a known problem with horizon drift on fixed wings. To ameliorate it, use `set imu_acc_ignore_rate = 10`. Setting this low is a good idea, but if it's set too low then the accelerometer will effectively be ignored and the horizon will eventually drift. To reduce the accelerometer's influence, you can also reduce `imu_dcm_ki` and/or `imu_dcm_kp`.

You can also try tuning `fw_turn_assist_pitch_gain`, although be careful to not set it too high because then the aircraft will stall trying to climb during a turn.

Adding a piece of black, porous foam (so wind can pass through) over the barometer has been known to help as well.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on January 01, 2021.  For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
