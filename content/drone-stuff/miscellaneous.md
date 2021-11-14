+++
title = "Miscellaneous"
weight = 8
sort_by = "weight"
insert_anchor_links = "right"
+++
This is a bunch of miscellaneous info that wouldn't fit anywhere else:

- The ZOHD Dart 250g with the stock motor draws 4.5A on 2S with the 5x5 propeller. It draws the same amperage at exactly 75% throttle with a 3S battery and the same propeller.
- When wiring your electronics, make sure you don't have any ground loops.
  This means that there should only be one ground wire going to each component.
  For example, the ESC has one ground wire for power (to the battery) and one for signal (to the FC), you should *only* use one of the two (the one going to the battery).
  What you can do for the other ground wire, though, is twist it around the signal wire and only connect it to the FC side, to reduce emissions.
  If you have coaxial cable, you can do the same, connect the outer shielding to the FC's ground, and don't connect the other side anywhere, and use the core as signal.
 - If you want to embed knurled nuts in foam so you can use screws, use a soldering iron. Set the iron to 150 C, put the nut on the tip of the iron, and push the nut into the foam. It will slowly melt the foam and embed itself quite firmly. Don't use a higher temperature or you'll open a larger hole and the nut won't fit snugly.
 - This is the command I used to flash an ESP8285 M3 with [esp-link](https://github.com/jeelabs/esp-link/ ):
   ```
   esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash -fs 1MB -fm dout \
                   0x00000 boot_v1.7.bin 0x1000 user1.bin \
                   0xFC000 esp_init_data_default.bin 0xFE000 blank.bin
   ```


## Motor and prop stuff

Here are the things I know about motors and propellers:

- The larger and steeper the propeller, the harder it is for the motor to turn.
- The more KV the motor is, the faster it turns, and the harder it is for it to turn.
- The harder the motor has to turn, the more current it draws, and the hotter it gets.
- The larger the (physical) size of the motor, the more heat it can dissipate.
- If the motor gets too hot, some part of it may melt. This ruins the motor.
- The smaller a propeller, the more quickly it can turn, and the more it can accelerate.
- The larger a propeller, the more efficient it is.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on November 15, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
