# Miscellaneous notes

These are random AP-related notes that wouldn't fit anywhere else:


## Performing an autotune

The [ArduPilot Autotune documentation](https://ardupilot.org/plane/docs/automatic-tuning-with-autotune.html) and the [demo video](https://www.youtube.com/watch?v=Ud_YPu7fgXE) are very detailed on this, but here's the gist on how to run an autotune.

Some things to know are:
- Autotune does not tune the rotation rates, but does not really depend on them either.
- You should set `AUTOTUNE_LEVEL` depending on the size of your aircraft. For small/agile craft, you can set `AUTOTUNE_LEVEL` to 7 or more. For larger, more sluggish craft, 6 (or less) is a good level. Under the hood, a higher `AUTOTUNE_LEVEL` decreases `*2SRV_TCONST` and increases `*2SRV_RMAX`).


Before you switch into `AUTOTUNE` mode, complete a circle or fly in different directions to allow the airspeed estimator to get an accurate value before running the autotune (or tuning the TECS). Don't start the tune unless your airspeed estimation is (and remains) stable and reasonable, otherwise you'll get bad results (and it probably means something is very wrong and you should land).

After you switch into `AUTOTUNE`, start with left and right roll inputs at maximum stick deflection. You don't need to wait until you hit the max roll angle, what I tend to do is roll max right, leave it for half a second, then roll max left, repeat.

The OSD will start showing you PID numbers, continue until a message saying `ROLL FINISHED` appears. Afterwards, do the same with pitch. Hit full stick deflection up and down, without reaching max pitch limits.

After the `PITCH FINISHED` message appears, continue flying in `AUTOTUNE` for more than ten seconds, to make sure the tune values are saved.

You're done, you can switch to any other mode and continue flying.

_(Thanks to Mike for the above info.)_


## DMA on the Matek F405-Wing

If you want to get DMA on UART3 of the Matek F405-Wing FC (or, more relatedly, the Racerstar F405, because UART1 is Bluetooth there), you can open `libraries/AP_HAL_ChibiOS/hwdef/MatekF405-Wing/hwdef.dat` and comment out line 92ish, where PA15 is defined.

That will enable DMA on UART3, at the expense of disabling the LED pad.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on January 26, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
