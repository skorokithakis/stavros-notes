+++
title = "Miscellaneous notes"
weight = 4
sort_by = "weight"
insert_anchor_links = "right"
+++
These are random AP-related notes that wouldn't fit anywhere else:

## DJI FPV configuration

If you got some DJI goggles, here's the relevant configuration you need to make:

1. Set `OSD_TYPE=3`.
2. Set `SERIALn_PROTOCOL=33 SERIALn_BAUD=115 SERIALn_OPTIONS=0` (DJI FPV).
3. Create a text file called `naco.txt` on the SD card of the Air Unit with the text `1` in it [to unlock full power](https://oscarliang.com/dji-fpv-system-fcc-700mw/).
4. Create a text file called `naco_pwr.txt` on the SD card of the goggles with the text `pwr_2` in it [to unlock more full power](https://oscarliang.com/dji-fpv-system-1200mw-output/).
5. Set "Custom OSD" to "on" in the goggles menu.
6. Arrange your OSD elements how you like them.

That's it!

## DMA on the Matek F405-Wing

If you want to get DMA on UART3 of the Matek F405-Wing FC (or, more relatedly, the Racerstar F405, because UART1 is Bluetooth there), you can open `libraries/AP_HAL_ChibiOS/hwdef/MatekF405-Wing/hwdef.dat` and comment out line 92ish, where PA15 is defined.

That will enable DMA on UART3, at the expense of disabling the LED pad.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on October 22, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
