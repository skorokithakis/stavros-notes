+++
title = "Ardupilot setup checklist"
weight = 2
sort_by = "weight"
insert_anchor_links = "right"
+++
This is a short guide for setting up [ArduPilot](https://ardupilot.org/) on a flying wing. I use an Omnibus F4 that was previously set up for INAV (so motor on 1, elevons on 3/4), so most of this guide will be geared to that. If you use a different controller, your mileage may vary.

You should keep the [full list of ArduPilot parameters](https://ardupilot.org/plane/docs/parameters.html) open, for your reference while tuning. 


## Building ArduPilot

Because building ArduPilot is a bit complicated, I've written a short script that uses Docker to build AP in a controlled environment.

Copy it from here, save it to a file called `docker_build.sh` in the root of the ArduPilot repo, and run it with `docker_build.sh <your board>`. Output files will be stored in `build/<yourboard>/bin/`:

```bash
#!/usr/bin/env bash

set -euo pipefail

if [ $# -ne 1 ]
  then
    echo "No board supplied, run as ./docker_build.sh <board name> or ./docker_build.sh list"
    exit 1
fi

BOARD=$1

git submodule update --init --recursive

git checkout Dockerfile
echo "RUN pip install intelhex" >> Dockerfile
echo "RUN sudo apt-get update && sudo apt-get install -y gcc-arm-none-eabi" >> Dockerfile
echo "RUN sudo apt-get clean  && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*" >> Dockerfile

docker build . -t ardupilot
git checkout Dockerfile

docker run --rm -it -v "$(pwd)":/ardupilot ardupilot:latest ./waf configure --board="$BOARD"
docker run --rm -it -v "$(pwd)":/ardupilot ardupilot:latest ./waf build
```


## Hardware setup

The values in this section are specific to the Omnibus F4, but the settings aren't, so you'll usually need to adjust your outputs to your specific configuration but you probably won't need to skip many of the steps here.


- [ ] Connect GPS to UART 6 (SERIAL4). You don't need to do anything else for GPS, it should work out of the box.
- [ ] Connect Fport to a UART. I chose UART 3 (SERIAL2). If you want to use UART 1, you should set the RC input jumper to PPM on the F4 to disconnect the SBUS inverter from the pin.
- [ ] To get Fport working with UART 3, you need to set `BRD_ALT_CONFIG=1`, to get UART 3 to act like a UART instead of I2C on the Omnibus F4.
- [ ] Change the board orientation with `AHRS_ORIENTATION`.
- [ ] Set the following for Fport on UART 3:
  ```
  SERIAL2_PROTOCOL = 23 (RCIN)
  SERIAL2_BAUD=115
  SERIAL2_OPTION=4
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
- [ ] Set the board orientation with `AHRS_TRIM_Y` and check that FBWA mode flies level.
- [ ] If you don't use logging, set `LOG_BACKEND_TYPE=0`.
- [ ] Check the preflight errors to warn on, though usually leaving it set to "all" is fine.
- [ ] Set up the OSD (Mission Planner has a very nice UI for that). Keep in mind that ArduPilot's airspeed and windspeed estimation are quite good, so you may want to add those even if you don't have an airspeed sensor. You may also want to set up multiple screens, I use a potentiometer to switch between the four different screens of the OSD:
  -  One with everything on (for debugging), which is also set as the `OSD_ARM_SCR`/`OSD_DSARM_SCR`.
  -  One with the artificial horizon, system messages and some basic info like RSSI, battery, ground speed and altitude.
  -  A minimal screen with just system messages and battery/RSSI/speed/altitude.
  -  A screen with just system messages, for when I want to enjoy the scenery.


## Radio-related

- [ ] Set your radio channels to AETR and run the radio calibration in the calibration section of ArduPilot.
- [ ] Add arming switch with `RCn_OPTION=41` (on whatever channel you want).
- [ ] Set up modes, possibly having switches override the mode channel to the mode you want.  
  What I do is set a given channel as the mode channel, and make that channel always output -100% on the radio. Then, I set up channel overrides for each switch, keeping in mind that overrides in OpenTX are executed in order (so the bottom override has the highest priority).  
  That way, I set MANUAL/ACRO/FBWA to be lowest priority (on the same switch), then CRUISE to override those, then LOITER, AUTO, AUTOTUNE in that order.  
  Finally, I add RTL to a switch on its own channel, with the highest priority of all overrides. I also add an override for that switch to the mode channel to -100%, so moving any other stick won't exit RTL mode as long as RTL is enabled.


## Auto modes

- [ ] Set `SERVO_AUTO_TRIM=1` so the aircraft trims itself while flying.
- [ ] Set `FS_SHORT_ACTN`/`FS_SHORT_TIMEOUT`/`FS_LONG_ACTN`/`FS_LONG_TIMEOUT`. I tend to disable the short action and set long to RTL.
- [ ] Set `RTL_CLIMB_MIN=30` so the aircraft climbs first before starting to return to home.
- [ ] Set `ACRO_LOCKING=1` to avoid drifting when you aren't moving the sticks.
- [ ] Change `AUTOTUNE_LEVEL` according to how aggressive you want the tune.
- [ ] Set `ACRO_PITCH_RATE`/`ACRO_ROLL_RATE` according to your craft.
- [ ] Set `THR_PASS_STAB=1` so you have total throttle control in ACRO/FBWA/STABILIZE.
- [ ] Set `ARSPD_FBW_MIN`/`ARSPD_FBW_MAX` to the minimum and maximum airspeed you want auto modes to fly.
- [ ] Set `MIN_GNDSPD_CM` so the craft makes an effort to return even under high winds. WARNING: Might make throttle pulse or have other unwanted side-effects.


## Auto takeoff

- [ ] Change `TKOFF_THR_MAX` to the desired max takeoff throttle.
- [ ] Change `TKOFF_ALT` to the altitude you want takeoff to reach.
- [ ] Set `THR_SUPP_MAN=1` so you can manually set the autolaunch "idle" throttle (before the throw).
- [ ] Set `TKOFF_THR_MINACC=18` for the takeoff throw to activate takeoff with a minimum of 2g.
- [ ] set `TKOFF_LVL_PITCH` to your desired angle (20 is a good value).
- [ ] Set `TKOFF_THR_DELAY` to the number of deciseconds that you want the motor to wait before it starts up.
- [ ] Potentially set `TKOFF_THR_SLEW=127` to make the throttle spin up to full faster (within 0.8 sec).


## Tuning the TECS

To tune the TECS, read the [TECS tuning guide](https://ardupilot.org/plane/docs/tecs-total-energy-control-system-for-speed-height-tuning-guide.html). It's very well-written and comprehensible. Note the maximum pitch up/down you want your plane to fly at (depending on the max vertical speed you want), and tune based on that.

## In the field

- [ ] Run an autotune.
- [ ] Fly in FBWA and see if you're gaining/losing altitude. Pitch up/down to fly level, check the pitch on the OSD, and use the formula `old_value+pitch*π/180` to get the new value (in radians).


_(Many thanks to Michel Pastor for his help with everything in this note.)_

* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 24, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
