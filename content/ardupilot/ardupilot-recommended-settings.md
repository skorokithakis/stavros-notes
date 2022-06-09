# ArduPilot recommended settings

This section contains some recommended settings for ArduPilot. Nothing is set in stone, these are just some defaults I've found to work well.

## GPS

```js
GPS_GNSS_MODE=71  # Enable GPS/SBAS/Galileo/GLONASS.
GPS_RATE_MS=100   # 10 Hz update rate.
```

## Crossfire/ELRS

```js
SERIALn_PROTOCOL=23  # Crossfire/ELRS.
RC_OPTIONS=800        # 5 - Arming check throttle.
                     # 8 - CRSF telemetry passthrough.
                     # 9 - Suppress CRSF mode/rate message for ELRS.
```

## Expo

30% expo is a good starting point:

```js
MAN_EXPO_ROLL=30
MAN_EXPO_PITCH=30
MAN_EXPO_RUDDER=30
```

## Miscellaneous

```js
INS_GYRO_FILTER=60     # Faster gyro updates.
SCHED_LOOP_RATE=100    # Faster scheduler updates.
```

## Servo update rate

If you want a higher servo update rate (because of digital servos), it is probably better to set the scheduler loop rate to the frequency you want, and enable ONESHOT on the servos:

```js
SCHED_LOOP_RATE=200   # As above.
ONESHOT_MASK=6        # Change to whatever channels your servos are on.
```

## Switch arming

If you want to use switch arming rather than stick arming, here are the relevant parameters:

```js
RCx_OPTION=153
ARMING_RUDDER=0
```

* * *

<p style="font-size:80%; font-style: italic">
Last updated on June 09, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
