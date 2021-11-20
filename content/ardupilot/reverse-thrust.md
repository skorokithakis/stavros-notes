# Reverse thrust

To set up reverse thrust (for higher braking when landing, for example), follow the steps below:

- [ ] Set your BLHeli-compatible ESC to "Reversible soft" and make sure you're using DShot.
- [ ] Set `THR_MIN=-100`.
- [ ] Set `SERVO_BLH_REMASK=1` (or whatever channel your motor is on).
- [ ] Set `RC9_OPTION=64` for the reversing switch on channel 9 (or whatever channel you want).
- [ ] Set `USE_REV_THRUST=0` to disable reverse thrust on all auto modes.

You're done.

When flipping the switch, throttle will reverse, so your plane will slow down instead of speed up the more you throttle up.
Be careful not to stall or otherwise hurt your craft, I don't recommend going over 20-30% reverse throttle.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 07, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
