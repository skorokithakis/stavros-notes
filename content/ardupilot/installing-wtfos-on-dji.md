# Installing WTFOS on DJI

The WTFOS OSD is basically a higher-res analog OSD that you can get on DJI goggles. It gives you everything the analog OSD gives you, so configuration menus, OSD elements, post-flight details, etc.

Here's the process to install it:

## On everything
* Make sure you're on version V01.00.0606 on whatever you want to root.
* If you're rooting an AU or Vista, use a fan to cool it down during this process.
* Go to [the WTFOS Configurator's Root section](https://fpv.wtf/root) and click "Root device". Click on your device on the permission popup and continue. Wait until done. DO NOT REBOOT WHEN IT'S DONE.
* Once that's done, go to [the WTFOS Installer section](https://fpv.wtf/wtfos) and click "connect to device", and then "Install WTFOS".
* After that's done, and if you're upgrading the goggles, go to [the Package Manager section](https://fpv.wtf/packages), and install `fcc-unlock` (for full power) and `msp-osd`. You can also install `auto-record` on the goggles, for automatically recording if your video link goes away and comes back. The rest probably isn't necessary.

## On the goggles
* Disable the custom OSD: Settings -> Display -> Custom OSD: Off.
* Download the font files [from the ArduCustom repository](https://github.com/ArduCustom/ardupilot/tree/master_custom/libraries/AP_OSD/fonts/HDFonts). Make sure to get the four fonts ending in `.bin`.
* If they aren't already, rename them to add `_ardu` to the name after `font` (so `font_ardu.bin`, `font_ardu_2.bin`, `font_ardu_hd.bin`, `font_ardu_hd_2.bin`).
* Put the four font files in the root of the goggles' SD card.

## On the plane
* Set `SERIALn_PROTOCOL=42` for DisplayPort, `OSD_TYPE=5` for MSP_DISPLAYPORT and `OSDn_TXT_RES=1` for 50x18 text resolution on the craft.
* Arrange your OSD elements as you want them.

That's all!

* * *

<p style="font-size:80%; font-style: italic">
Last updated on November 27, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
