+++
title = "ArduPilot recommended settings"
weight = 1
sort_by = "weight"
insert_anchor_links = "right"
+++
This section contains some recommended settings for ArduPilot. Nothing is set in stone, these are just some defaults I've found to work well.

## GPS

```
GPS_GNSS_MODE=71  # Enable GPS/SBAS/Galileo/GLONASS.
GPS_RATE_MS=100   # 10 Hz update rate.
```

## Crossfire/ELRS

```
SERIALn_PROTOCOL=23  # Crossfire/ELRS.
RC_OPTION=800        # 5 - Arming check throttle.
                     # 8 - CRSF telemetry passthrough.
                     # 9 - Suppress CRSF mode/rate message for ELRS.
```

## Miscellaneous

```
INS_GYRO_FILTER=60     # Faster gyro updates.
SCHED_LOOP_RATE=100    # Faster scheduler updates.
```

* * *

<p style="font-size:80%; font-style: italic">
Last updated on October 30, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
