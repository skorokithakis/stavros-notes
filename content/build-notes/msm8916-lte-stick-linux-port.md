# MSM8916 LTE stick Linux port

**Project:** Running Linux on a cheap MSM8916-based 4G LTE dongle using the OpenStick project.

## Details

- Chip: Qualcomm MSM8916, 4x 1.0 GHz Cortex-A53
- RAM: 512MB, Storage: 4GB or 8GB eMMC
- Features: WiFi, GPS, LTE modem, Bluetooth (hardware-dependent)
- Frequency bands: 4G FDD LTE B1/3/5, 3G WCDMA B1
- Size: ~95x33mm, transmission rate: 150Mbps
- Ships with Android 4.4.4, reflashable to mainline Linux
- Common variants: UZ801 V3.0/V3.2, UFI001B/C, UFI003, UFI103S, UF896, SP970
- Default management IPs: 192.168.43.1:8080 (white) or 192.168.100.1 (black)

### Flashing notes

- Enter EDL mode: `adb reboot edl` or short EDL testpoint whilst inserting USB
- UZ801 V3.0: Enable ADB at http://192.168.100.1/usb_debug.html
- UZ801 V3.2: Enable ADB at http://192.168.100.1/usbdebug.html
- UART voltage: 1.8V for UZ801, 3.3V for UFI models
- Backup eMMC before flashing (using bkerler/EDL tool)
- May need to replace firmware files in /lib/firmware for modem to work properly

## Resources

- [AliExpress listing](https://www.aliexpress.com/item/1005006924641101.html)
- [OpenStick GitHub](https://github.com/OpenStick/OpenStick)
- [OpenStick Wiki](https://www.kancloud.cn/handsomehacker/openstick/content)
- [PostmarketOS wiki](https://wiki.postmarketos.org/wiki/Zhihe_series_LTE_dongles_) - Detailed technical info
- [Wim van 't Hoog's guide](https://wvthoog.nl/openstick/) - Comprehensive guide with Debian Bookworm build, USB Gadget examples, pentesting applications
- [HN discussion](https://news.ycombinator.com/item?id=45252817)

## Log

- **2025-12-27:** Purchased MSM8916-based LTE stick from AliExpress.
- **2025-12-27:** Researched OpenStick project, PostmarketOS wiki, and Wim van 't Hoog's guide.
- **2025-12-27:** Backed up eMMC via EDL, flashed Linux firmware. Flash successful - Linux booting on the stick!

* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 23, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
