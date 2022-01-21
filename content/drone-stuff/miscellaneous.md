# Miscellaneous

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
- Propellers have a direction: The top usually has letters like, for example, "6040" (which denotes the size and pitch of the propeller), and the top needs to always point towards where the plane will be flying (the front). No matter if you have a pusher or puller, the top of the propeller needs to be pointing forward.
- When it comes to cameras/standards, the difference between PAL and NTSC is that PAL has higher resolution (625 lines, ie 576i for PAL vs 525 lines, ie 480i for NTSC), but lower framerate (25 fps for PAL vs 29.97 fps for NTSC). I use PAL because I prefer having higher resolution.
- If doing manual/hand launches of planes/wings, you'll notice that you need to have your hand on the pitch/roll stick when launching, which means you need to launch with your left hand, which is where the arm and throttle controls usually are. That makes it hard to throttle up to start the launch, or down (or disarm) in an emergency.  
To make things a bit easier, I set the back right switch (SG) to override the throttle and set it to the launch throttle (40% for me, for example). That way, I can arm, keep the throttle down, and flip SG with my right hand. That will throttle up enough to easily launch the wing, and if something goes wrong I can still either disarm or flip SG down so the motor stops again.
- ESCs that run on the DShot protocol don't need throttle calibration, you can go ahead and use them right away and they'll do the right thing.


## Motor and prop stuff

Here are the things I know about motors and propellers:

- The larger and steeper the propeller, the harder it is for the motor to turn.
- The more KV the motor is, the faster it turns, and the harder it is for it to turn.
- The harder the motor has to turn, the more current it draws, and the hotter it gets.
- The larger the (physical) size of the motor, the more heat it can dissipate.
- The more amps (current) the motor draws, the hotter it gets (proportional to the square of the current).
- If the motor gets too hot, some part of it may melt. This ruins the motor.
- The smaller a propeller, the more quickly it can turn, and the more it can accelerate.
- The larger a propeller, the more efficient it is.

## Recommended BLHeli ESC configuration for fixed wing

If you have a BLHeli/BLHeli32 ESC, these settings are recommended:

* Temperature protection: 90 C
* Motor timing: Auto
* Throttle cal enabled: Enabled
* Non-damped mode: Enabled
* Sine modulation mode: Enabled

* * *

<p style="font-size:80%; font-style: italic">
Last updated on January 21, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
