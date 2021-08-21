+++
title = "ArduPilot setup checklist"
weight = 2
sort_by = "weight"
insert_anchor_links = "right"
+++
This is a short guide for setting up [ArduPilot](https://ardupilot.org/) on a flying wing. I use an Omnibus F4 that was previously set up for INAV (so motor on 1, elevons on 3/4), so most of this guide will be geared to that. If you use a different controller, your mileage may vary.

You should keep the [full list of ArduPilot parameters](https://ardupilot.org/plane/docs/parameters.html) open, for your reference while tuning. 


## Helper utility


I have created a utility that lets you easily get/set/backup/restore parameters from the command line.
It's called Parachute, and you can download it here:

[https://gitlab.com/stavros/parachute](https://gitlab.com/stavros/parachute)


## Building ArduPilot

Because building ArduPilot is a bit complicated, I've written a short script that uses Docker to build AP in a controlled environment.

Copy it from here, save it to a file called `docker_build.sh` in the root of the ArduPilot repo, and run it with `docker_build.sh <your board>`. Output files will be stored in `build/<yourboard>/bin/`, and you can flash them with the [INAV configurator](https://github.com/iNavFlight/inav-configurator/releases) by putting your board in DFU mode and uploading the `arduplane_with_bl.hex` file:

```bash
#!/usr/bin/env bash

set -euo pipefail

if [ $# -ne 1 ]
  then
    echo "No board supplied, run as ./docker_build.sh <board name> or ./docker_build.sh list"
    exit 1
fi

BOARD=$1

cd "$(git rev-parse --show-toplevel)"

git submodule update --init --recursive

git checkout Dockerfile
echo "RUN pip install intelhex" >> Dockerfile
echo 'ENV PATH="/home/ardupilot/.local/bin:/usr/lib/ccache:/opt/gcc-arm-none-eabi-10-2020-q4-major/bin:/ardupilot/Tools/autotest:${PATH}"' >> Dockerfile
cat Dockerfile

docker build . -t ardupilot
git checkout Dockerfile

docker run --rm -it -v "$(pwd)":/ardupilot ardupilot ./waf configure --board="$BOARD"
docker run --rm -it -v "$(pwd)":/ardupilot ardupilot ./waf build
```


## Hardware setup

The values in this section are specific to the Omnibus F4, but the settings aren't, so you'll usually need to adjust your outputs to your specific configuration but you probably won't need to skip many of the steps here.


- [ ] Connect GPS to UART 6 (SERIAL4). You don't need to do anything else for GPS, it should work out of the box.
- [ ] Change the FC's orientation with `AHRS_ORIENTATION` and monitor the artificial horizon to see if it moves correctly.
- [ ] Calibrate the accelerometer. "Forward" here needs to be the forward direction of the plane, not the arrow on the FC.
- [ ] Connect Fport to a UART. I chose UART 3 (SERIAL2). If you want to use UART 1, you should set the RC input jumper to PPM on the F4 to disconnect the SBUS inverter from the pin.
- [ ] To get Fport working with UART 3, you need to set `BRD_ALT_CONFIG=1`, to get UART 3 to act like a UART instead of I2C on the Omnibus F4.
- [ ] Set the following for Fport on UART 3:
  ```
  SERIAL2_PROTOCOL = 23 (RCIN)
  SERIAL2_BAUD=115
  SERIAL2_OPTIONS=4
  RSSI_TYPE=3
  ```
- [ ] Once Fport works, reverse the elevator with `RC2_REVERSED=1`.
- [ ] Set up your servo functions and trims:
  ```
  SERVO1_FUNCTION=70
  SERVO1_MIN=1000
  SERVO1_MAX=2000
  SERVO1_TRIM=1000

  SERVO3_FUNCTION=77
  SERVO3_MIN=1000
  SERVO3_MAX=2000
  SERVO3_TRIM=1500

  SERVO4_FUNCTION=78
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
- [ ] Set `RTL_CLIMB_MIN=30` so the aircraft climbs first before starting to return to home.
- [ ] Set `ACRO_LOCKING=1` to avoid drifting when you aren't moving the sticks.
- [ ] Change `AUTOTUNE_LEVEL` according to how aggressive you want the tune.
- [ ] Set `ACRO_PITCH_RATE`/`ACRO_ROLL_RATE` according to your craft.
- [ ] Set `THR_PASS_STAB=1` so you have total throttle control in ACRO/FBWA/STABILIZE.
- [ ] Set `ARSPD_FBW_MIN`/`ARSPD_FBW_MAX` to the minimum and maximum airspeed you want auto modes to fly (see the TECS tuning guide below for details).
- [ ] Set `MIN_GNDSPD_CM` so the craft makes an effort to return even under high winds. WARNING: Might make throttle pulse or have other unwanted side-effects.


## Auto takeoff

- [ ] Change `TKOFF_THR_MAX` to the desired max takeoff throttle.
- [ ] Change `TKOFF_ALT` to the altitude you want takeoff to reach.
- [ ] Set `THR_SUPP_MAN=1` so you can manually set the autolaunch "idle" throttle (before the throw).
- [ ] Set `TKOFF_THR_MINACC=18` for the takeoff throw to activate takeoff with a minimum of 2g.
- [ ] Set `TKOFF_LVL_PITCH` to your desired angle (20 is a good value).
- [ ] Set `TKOFF_THR_DELAY` to the number of deciseconds that you want the motor to wait before it starts up.
- [ ] Potentially set `TKOFF_THR_SLEW=-1` to make the throttle spin up faster.


## In the field

- [ ] Run an autotune.
- [ ] Fly in FBWA and see if you're gaining/losing altitude. Pitch up/down to fly level, check the pitch on the OSD, and use the formula `old_value+pitch*π/180` to get the new value for `AHRS_TRIM_Y` (in radians).


## Tuning the TECS

To tune the TECS, a helpful resource is the [TECS tuning guide](https://ardupilot.org/plane/docs/tecs-total-energy-control-system-for-speed-height-tuning-guide.html).
Make sure you have run an autotune beforehand, and continue with the tuning below.

In tuning, there are three stages:

- Prepare to measure
- Take measurements in the field.
- Set parameters on the bench, based on your measurements.

### Preparation

- [ ] Set `LIM_PITCH_MAX=4500` (centidegrees), or something similarly high.
  This is the maximum pitch you'll be achieving in FBWA, and you don't want to be limited by this while trying to tune.
- [ ] Set `LIM_PITCH_MIN=-4500` (centidegrees) or something similarly low.
  This is the minimum pitch you'll be achieving in FBWA, and you don't want to be limited by this either.


### In the field

You should perform the measurements in four stages, all in the FBWA mode:

#### Fly straight

Fly straight and note down:

- [ ] The maximum speed you want to be flying at (in km/h).
- [ ] The throttle percentage at that maximum speed.
- [ ] Start a turn at the maximum bank angle (full roll deflection to one side) and note the slowest speed you can fly at without stalling.
- [ ] Fly straight at a speed 15% higher than the stall speed from the previous step, and note that speed. This is your trim speed.
- [ ] Note the throttle percentage at that speed.
- [ ] Turn throttle to 0 and pitch down a bit so you don't stall.
  Note the minimum amount of down-pitch required to keep you from stalling (this should only be in the 1-3 degree ballpark).

#### Fly up

Set the throttle to the maximum throttle percentage from the previous step and start slowly pitching up until your airspeed equals your trim speed from the previous step.
If you're higher than that speed and need to climb more, change `LIM_PITCH_MAX` to something higher and try again.
Note down:

- [ ] The pitch angle (in degrees).
- [ ] The vertical speed from the variometer (in m/s).

#### Fly down

Set the throttle to 0 and start pitching down until your airspeed equals your trim speed from the previous step.
Note down:

- [ ] The vertical speed from the variometer (in m/s).

#### Fly down more

Keep the throttle at 0 and pitch down until you reach your desired maximum speed from step 1.
If you're lower than that speed and need to pitch down more, change `LIM_PITCH_MIN` to something lower and try again.
Note down:

- [ ] The pitch angle (in degrees).
- [ ] The vertical speed from the variometer (in m/s).

You're done with this step.


### On the bench

After you have the above measurements, you're ready to tune things.

You can either do things manually (below), or use the [TECS tuning calculator](../../drone-stuff/tecs-tuning-calculator) to get the appropriate parameters automatically.

For the level flight measurements:

- [ ] Set `ARSPD_FBW_MAX` (m/s) to something a bit less than the maximum airspeed you achieved in level flight.
- [ ] Set `THR_MAX` (percentage) to the throttle percentage at max speed.
- [ ] Set `ARSPD_FBW_MIN` (m/s) to the slowest speed you could turn at without stalling (maybe go a bit higher for some margin).
- [ ] Set `TRIM_ARSPD_CM` (cm/s) to your trim speed.
- [ ] Set `TRIM_THROTTLE` (percentage) to your trim throttle percentage.
- [ ] Set `STAB_PITCH_DOWN` (degrees) to the pitch angle that keeps you from stalling.

For the ascent measurements:

- [ ] Set `TECS_PITCH_MAX` (degrees) to the pitch angle you measured.
- [ ] Set `TECS_CLMB_MAX` and `FBWB_CLIMB_RATE` (both in m/s) to the climb rate you measured.

For the descent measurements:

- [ ] Set `TECS_SINK_MIN` (m/s) to the descent rate you measured.

For the max descent measurements:

- [ ] Set `TECS_PITCH_MIN` (degrees) to the pitch angle you measured.
- [ ] Set `TECS_SINK_MAX` (m/s) to the descent rate you measured.

That's it!


## Reverse thrust

To set up reverse thrust (for higher braking when landing, for example), follow the steps below:

- [ ] Set your BLHeli-compatible ESC to "Reversible soft" and make sure you're using DShot.
- [ ] Set `THR_MIN=-100`.
- [ ] Set `SERVO_BLH_REMASK=1` (or whatever channel your motor is on).
- [ ] Set `RC9_OPTION=64` for the reversing switch on channel 9 (or whatever channel you want).
- [ ] Set `USE_REV_THRUST=0` to disable reverse thrust on all auto modes.

You're done.

When flipping the switch, throttle will reverse, so your plane will slow down instead of speed up the more you throttle up.
Be careful not to stall or otherwise hurt your craft, I don't recommend going over 20-30% reverse throttle.


## Parachute parameters

This is the regex I use with Parachute to transfer between planes only the parameters that are transferrable (ie non-plane-specific):

`^(ACRO_LOCKING|OSD.*|RC[\d_]+.*|FLTMODE.*|FLIGHT_OPTIONS|FS_.*|RTL_CLIMB_MIN|RTL_RADIUS|THR_PASS_STAB|THR_SLEWRATE|THR_SUPP_MAN|TKOFF_ACCEL_CNT|TKOFF_ALT|TKOFF_DIST|TKOFF_THR_DELAY|HOME_RESET_ALT|ALT_HOLD_RTL)$`

This will transfer things like the OSD settings, flight modes, failsafe options, etc etc, but will leave things like PID tuning alone.
Use it to set up a new plane by copying over settings from an older plane.

_(Many thanks to Michel Pastor for his help with everything in this note.)_

* * *

<p style="font-size:80%; font-style: italic">
Last updated on August 21, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
