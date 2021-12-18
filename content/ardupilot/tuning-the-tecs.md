# Tuning the TECS

To tune the TECS, a helpful resource is the official [TECS tuning guide](https://ardupilot.org/plane/docs/tecs-total-energy-control-system-for-speed-height-tuning-guide.html).
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
- [ ] Set `THR_PASS_STAB=1` to avoid mapping your throttle to a curve in some modes. This is important because you want a raw (non-remapped) throttle value when measuring.
- [ ] Add the airspeed and pitch angle elements to the OSD so you can actually take the measurements.
- [ ] Enable throttle battery voltage compensation with `FWD_BAT_VOLT_MIN`/`FWD_BAT_VOLT_MAX`. Set the max to `4.2 * num_cells` and the min to `3 * num_cells` for Li-Ion and `3.5 * num_cells` for LiPo batteries. This makes your measurements more accurate, as a partially-depleted battery won't make your motor run slower and skew the results.


### In the field
You should perform the measurements in four stages, all in the FBWA mode:

#### Fly straight
Fly straight and note down:

- [ ] The maximum speed you want to be flying at (in km/h).
- [ ] The throttle percentage at that maximum speed. Use the stick position, not the OSD item.
- [ ] Start a turn at the maximum bank angle (full roll deflection to one side) and note the slowest speed you can fly at without stalling.
- [ ] Fly straight at a speed 15% higher than the stall speed from the previous step, and note that speed. This is your trim speed.
- [ ] Note the throttle percentage at that speed. Use the stick position, not the OSD item.
- [ ] Turn throttle to 0 and pitch down a bit so you don't stall.
  Note the minimum amount of down-pitch required to keep you from stalling (this should only be in the 1-3 degree ballpark).

#### Fly up
Set the throttle stick to the maximum throttle percentage from the previous step and start slowly pitching up until your airspeed equals your trim speed from the previous step.
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
After you have the above measurements, you're ready to tune things. You can use the automatic calculator:

### [TECS tuning calculator](/ardupilot/tecs-tuning-calculator.html)

Otherwise, you can do things manually, following the steps below, but you should really use the calculator instead.

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


## Advanced information

This is some more advanced information on tuning the TECS:

- If you want more altitude precision and more responsive control, you should lower the `TECS_SPDWEIGHT` parameter value below 1.
- A right `KFF_THR2PTCH` value is crucial for the TECS to work correctly without pitot.
- The `THR_SLEWRATE` value should be set so that the plane doesn't lose airspeed when you yank the pitch stick to `TECS_CLMB_MAX` degrees.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 18, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
