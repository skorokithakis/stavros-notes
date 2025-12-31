# MSM8916 LTE stick Linux port

**Project:** Running Linux on an MSM8916-based 4G LTE dongle

**Description:** Porting Linux to a Chinese MSM8916-based 4G modem stick using the OpenStick project. These are cheap LTE dongles (Zhihe series, UZ801, UFI models) that ship with Android 4.4.4 but can run mainline Linux. The OpenStick project provides reverse engineering and mainline Linux support for these devices.

**Device specs (from AliExpress listing):**
- Chip: Qualcomm 8916 (MSM8916)
- Frequency bands: 4G FDD LTE B1/3/5, 3G WCDMA B1
- Size: ~95x33mm
- Transmission rate: 150Mbps
- Default management IPs vary by colour: 192.168.43.1:8080 (white) or 192.168.100.1 (black)

**Common device variants:**
- UZ801 V3.0, V3.2 (most common currently sold)
- UFI001B, UFI001C, UFI003, UFI103S
- UF896
- SP970

**Hardware details:**
- CPU: 4x 1.0 GHz Cortex-A53
- RAM: 512MB
- Storage: 4GB or 8GB eMMC
- Features: WiFi, GPS, LTE modem, Bluetooth (hardware-dependent)

**Resources:**
- OpenStick GitHub: https://github.com/OpenStick/OpenStick
- OpenStick Wiki: https://www.kancloud.cn/handsomehacker/openstick/content
- PostmarketOS wiki (detailed technical info): https://wiki.postmarketos.org/wiki/Zhihe_series_LTE_dongles_
- Wim van 't Hoog's comprehensive guide: https://wvthoog.nl/openstick/
- HN discussion: https://news.ycombinator.com/item?id=45252817

**Key technical notes:**
- Entering EDL mode: `adb reboot edl` or short EDL testpoint whilst inserting USB
- UZ801 V3.0: Enable ADB at http://192.168.100.1/usb_debug.html
- UZ801 V3.2: Enable ADB at http://192.168.100.1/usbdebug.html
- UART voltage: 1.8V for UZ801, 3.3V for UFI models
- Backup eMMC before flashing (using bkerler/EDL tool)
- May need to replace firmware files in /lib/firmware for modem to work properly

---

## Log

- **2025-12-27**: Purchased MSM8916-based LTE stick from AliExpress (https://www.aliexpress.com/item/1005006924641101.html)
- **2025-12-27**: Researching OpenStick project for Linux installation
- **2025-12-27**: Found Wim van 't Hoog's detailed guide with Debian Bookworm build, USB Gadget examples, and pentesting applications
- **2025-12-27**: Confirmed device is Qualcomm 8916, supports LTE bands B1/3/5
- **2025-12-27**: Reviewed PostmarketOS wiki - comprehensive technical documentation with partition layouts, firmware flashing procedures, and device-specific quirks
- **2025-12-27**: Following guide, backing up eMMC via EDL
- **2025-12-27**: Backup complete, flashing Linux firmware
- **2025-12-27**: Flash successful — Linux booting on the stick!

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 27, 2025. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
