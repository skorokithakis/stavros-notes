# DJI FPV configuration

## Configuring ArduPilot for DJI FPV

If you're using the DJI FPV system, here's the relevant configuration you need to set:

1. Set `OSD_TYPE=3`.
2. Set `SERIALn_PROTOCOL=33 SERIALn_BAUD=115 SERIALn_OPTIONS=0` (DJI FPV).
3. Create a text file called `naco.txt` on the SD card of the Air Unit with the text `1` in it [to unlock full power](https://oscarliang.com/dji-fpv-system-fcc-700mw/).
4. Create a text file called `naco_pwr.txt` on the SD card of the goggles with the text `pwr_2` in it [to unlock more full power](https://oscarliang.com/dji-fpv-system-1200mw-output/).
5. Set "Custom OSD" to "on" in the goggles menu.
6. Arrange your OSD elements how you like them.

That's it!

## Configuring AP for the DJI O3

If you're using DJI O3, this is what you need to do:

* Set , `OSD_TYPE=5` for MSP_DISPLAYPORT.
* Set `SERIALn_PROTOCOL=42 SERIALn_BAUD=115 SERIALn_OPTIONS=0` for DisplayPort.
* Set `MSP_OPTIONS=5` for telemetry mode and BTFL fonts.
* Arrange your OSD elements as you want them.

Done!

## Synchronizing the video and audio of the DJI Air Unit

The audio of the DJI air unit is slower than the video, leading to desynchronization, but it is slower by a constant factor, which means it can be easily corrected with the following command:

```bash
$ ffmpeg -i "$1" -c:v copy -filter:a atempo=1.001480,volume=20 \
         -c:a aac -b:a 93k "$(basename "$1" .mp4)_fixed_audio.mp4"
```

* * *

<p style="font-size:80%; font-style: italic">
Last updated on May 03, 2025. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
