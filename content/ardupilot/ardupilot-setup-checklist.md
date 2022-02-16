# ArduPilot setup checklist

This is a short guide for setting up [ArduPilot](https://ardupilot.org/) on a flying wing. I use an Omnibus F4 that was previously set up for INAV (so motor on 1, elevons on 3/4), so most of this guide will be geared to that. If you use a different controller, your mileage may vary.

You should keep the [full list of ArduPilot parameters](https://ardupilot.org/plane/docs/parameters.html) open, for your reference while tuning. 


## Helper utility
I have created a utility that lets you easily get/set/backup/restore parameters from the command line.
It's called Parachute, and you can download it here:

[https://gitlab.com/stavros/parachute](https://gitlab.com/stavros/parachute)


## Building ArduPilot
See [Building ArduPilot](/ardupilot/building-ardupilot.html) for instructions on how to build the latest version.


## Hardware setup
The values in this section are specific to the Omnibus F4, but the settings aren't, so you'll usually need to adjust your outputs to your specific configuration but you probably won't need to skip many of the steps here.


- [ ] Connect GPS to UART 6 (SERIAL4). You don't need to do anything else for GPS, it should work out of the box. If it doesn't, set `SERIALn_PROTOCOL=5`.
- [ ] Change the FC's orientation with `AHRS_ORIENTATION` and monitor the artificial horizon to see if it moves correctly.
- [ ] Calibrate the accelerometer. "Forward" here needs to be the forward direction of the plane, not the arrow on the FC.
- [ ] Connect Fport to a UART. I chose UART 3 (SERIAL2). If you want to use UART 1, you should set the RC input jumper to PPM on the F4 to disconnect the SBUS inverter from the pin.
- [ ] To get Fport working with UART 3, you need to set `BRD_ALT_CONFIG=1`, to get UART 3 to act like a UART instead of I2C on the Omnibus F4.
- [ ] Set the following for Fport on UART 3:
  ```js
  SERIAL2_PROTOCOL=23  # RCIN
  SERIAL2_BAUD=115
  SERIAL2_OPTIONS=4
  RSSI_TYPE=3
  ```
- [ ] Once Fport works, reverse the elevator with `RC2_REVERSED=1`.
- [ ] Set up your servo functions and trims:
  ```js
  SERVO1_FUNCTION=70  # Throttle
  SERVO1_MIN=1000
  SERVO1_MAX=2000
  SERVO1_TRIM=1000

  SERVO3_FUNCTION=77  # Left elevon
  SERVO3_MIN=1000
  SERVO3_MAX=2000
  SERVO3_TRIM=1500

  SERVO4_FUNCTION=78  # Right elevon
  SERVO4_MIN=1000
  SERVO4_MAX=2000
  SERVO4_TRIM=1500
  ```
  All these values are necessary, because usually the `SERVOn_TRIM` won't be at 1500.
- [ ] Set `SERVO_BLH_OTYPE=4` for DShot150 and `SERVO_BLH_MASK=1` to enable it for the motor.
- [ ] Set `COMPASS_ENABLE=0` if you don't have a compass, otherwise calibrate it (not detailed here).
- [ ] Set `TERRAIN_ENABLE=0` to get rid of the terrain warning.
- [ ] Set the FC's pitch relative to the body with `AHRS_TRIM_Y` and check that FBWA mode flies level.
- [ ] If you don't use logging, set `LOG_BACKEND_TYPE=0`.
- [ ] Check the preflight errors to warn on, though usually leaving it set to "all" is fine.
- [ ] Set up the OSD (Mission Planner has a very nice UI for that). Keep in mind that ArduPilot's airspeed and windspeed estimation are quite good, so you may want to add those even if you don't have an airspeed sensor. You may also want to set up multiple screens, I use a potentiometer to switch between the four different screens of the OSD:
  -  One with everything on (for debugging), which is also set as the `OSD_ARM_SCR`/`OSD_DSARM_SCR`.
  -  One with the artificial horizon, system messages and some basic info like RSSI, battery, ground speed and altitude.
  -  A minimal screen with just system messages and battery/RSSI/speed/altitude.
  -  A screen with just system messages, for when I want to enjoy the scenery.


## Radio-related
- [ ] Set your radio channels to AETR and run the radio calibration in the calibration section of ArduPilot.
- [ ] Add a killswitch to the radio that overrides the mode to manual and the throttle to 0.
  This way it's really easy to kill the motor right away, but you still need to go through the arming procedure to get the motor running (thanks to Michel Pastor for this great idea).
- [ ] Set up modes, possibly having switches override the mode channel to the mode you want.  
  What I do is set a given channel as the mode channel, and make that channel always output -100% on the radio. Then, I set up channel overrides for each switch, keeping in mind that overrides in OpenTX are executed in order (so the bottom override has the highest priority).  
  That way, I set MANUAL/ACRO/FBWA to be lowest priority (on the same switch), then CRUISE to override those, then LOITER, RTL in that order.  Finally, I add AUTO to a switch on its own channel.  
  Keep in mind that whatever mode you have on its own channel might be overridden if you flick a different switch.
  Unfortunately, the way the mode system in AP works, there's no good way to have a list of prioritized modes, which would be ideal though now I have opened a PR to extend the modes to 12, which solves this).


## Auto modes
- [ ] Set `SERVO_AUTO_TRIM=1` so the aircraft trims itself while flying.
- [ ] Set `FS_SHORT_ACTN`/`FS_SHORT_TIMEOUT`/`FS_LONG_ACTN`/`FS_LONG_TIMEOUT`. I tend to disable the short action and set long to RTL.
- [ ] Set `FLIGHT_OPTIONS+=16` so the aircraft climbs first before starting to return to home.
- [ ] Set `ACRO_LOCKING=1` to avoid drifting when you aren't moving the sticks.
- [ ] Change `AUTOTUNE_LEVEL` according to how aggressive you want the tune.
- [ ] Set `ACRO_PITCH_RATE`/`ACRO_ROLL_RATE` according to your craft.
- [ ] Set `THR_PASS_STAB=1` so you have total throttle control in ACRO/FBWA/STABILIZE.
- [ ] Set `ARSPD_FBW_MIN`/`ARSPD_FBW_MAX` to the minimum and maximum airspeed you want auto modes to fly (see the TECS tuning guide below for details).
- [ ] Set `MIN_GNDSPD_CM=833` (30 km/h) so the craft makes an effort to return even under high winds.


## Auto takeoff
- [ ] Change `TKOFF_THR_MAX` to the desired max takeoff throttle.
- [ ] Change `TKOFF_ALT` to the altitude you want takeoff to reach.
- [ ] Set `THR_SUPP_MAN=1` so you can manually set the autolaunch "idle" throttle (before the throw).
- [ ] Set `TKOFF_THR_MINACC=18` for the takeoff throw to activate takeoff with a minimum of 2g.
- [ ] Set `TKOFF_LVL_PITCH` to your desired angle (20 is a good value).
- [ ] Set `TKOFF_THR_DELAY` to the number of deciseconds that you want the motor to wait before it starts up.
- [ ] Set `FLIGHT_OPTIONS+=64` so the aircraft doesn't oscillate on auto takeoff without an airspeed sensor.
- [ ] Potentially set `TKOFF_THR_SLEW=-1` to make the throttle spin up faster.

## Recommended settings.

See the [recommended settings](/ardupilot/ardupilot-recommended-settings.html) page for other recommended defaults.

## In the field
- [ ] Run an [autotune](/ardupilot/miscellaneous-notes.html).
- [ ] Fly in FBWA and see if you're gaining/losing altitude. Pitch up/down to fly level, check the pitch on the OSD, and use the formula `old_value+pitch*π/180` to get the new value for `AHRS_TRIM_Y` (in radians).
- [ ] After you set `AHRS_TRIM_Y` correctly above, fly in FBWA at full throttle (or whatever throttle you feel is "full" enough, and note that value), and note the pitch you need so that the wing doesn't climb or sink. Then, set `KFF_THR2PITCH` with the formula `pitch_value_in_deg * 100 / throttle_percentage`. `pitch_value_in_deg` should be positive if you needed up pitch and negative if you needed down pitch.

_(Many thanks to Michel Pastor for his help with everything in this note.)_

* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 16, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
