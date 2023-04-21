# Installing BLTouch-compatible firmware onto the TwoTrees Sapphire Pro

I installed a BLTouch/3D Touch probe onto my TwoTrees Sapphire Pro, and configuring the firmware was a bit involved. Here's the process:

* Clone the [Marlin repo from GitHub](https://github.com/MarlinFirmware/Marlin).
* Download [the configurations](https://github.com/MarlinFirmware/Configurations/archive/bugfix-2.1.x.zip).
* Checkout the `2.1` branch (the configurations seem to be tailored to it and I couldn't be bothered changing).
* Replace the `Configuration.h` and `Configuration_adv.h` files with the ones from the configurations zip.
* Uncomment the `SPRO_BLTOUCH` define.
* I also changed my dimensions to `X_BED_SIZE 230` and `Y_BED_SIZE 225`, for a more realistic bed size.
* Build with `pio run -e mks_robin_nano35`.
* Copy `.pio/build/mks_robin_nano35/Robin_nano35.bin` to the SD card.
* Insert the card into the printer and turn it on.
* Done!

* * *

<p style="font-size:80%; font-style: italic">
Last updated on April 21, 2023. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
