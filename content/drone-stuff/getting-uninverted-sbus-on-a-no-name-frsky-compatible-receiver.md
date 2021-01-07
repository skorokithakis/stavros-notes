+++
title = "Getting uninverted SBUS on a no-name FrSky-compatible receiver"
weight = 4
sort_by = "weight"
insert_anchor_links = "right"
+++
I got an [RC receiver](https://www.banggood.com/2_4G-8CH-D8-Mini-FrSky-Compatibel-Receiver-With-PWM-PPM-SBUS-Output-p-1140478.html?rmmds=myorder&cur_warehouse=CN) from Banggood. There's uninverted SBUS on this pad:

[![rc-sbus.jpg](../../resources/ccc7571db5d147328860077fdc0aa745.jpg)](../../resources/ccc7571db5d147328860077fdc0aa745.jpg)

To break this out to the SBUS pad, I had to remove/bridge the resistor that is circled in the image, and remove/bridge the FET on the other side:

[![rc-sbus-mosfet.jpg](../../resources/1b0f508a533e45b496c6636d49161b0c.jpg)](../../resources/1b0f508a533e45b496c6636d49161b0c.jpg)



* * *

<p style="font-size:80%; font-style: italic">
Last updated on November 24, 2020.  For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
