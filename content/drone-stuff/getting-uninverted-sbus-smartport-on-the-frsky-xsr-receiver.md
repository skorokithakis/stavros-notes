+++
title = "Getting uninverted SBUS/SmartPort on the FrSky XSR receiver"
weight = 6
sort_by = "weight"
insert_anchor_links = "right"
+++
To get uninverted SBUS/SmartPort on the FrSky XSR/X4RS receiver, you can repurpose the CPPM pad.
Remove the two small resistors shown in the image, and solder the two lower pads (together) to either the CPPM pad or the MOSFET pin shown in the photo:

[![xsr-sbus.jpeg](../../resources/f86da9a7aac1413ebd77825897164f7f.jpg)](../../resources/f86da9a7aac1413ebd77825897164f7f.jpg)

They should be soldered like this (remember to solder both resistor pads together):

[![xsr-sbus2.jpeg](../../resources/815576429ece43789dbc70dfd33517a1.jpg)](../../resources/815576429ece43789dbc70dfd33517a1.jpg)

Now the CPPM pad will be uninverted SBUS/SmartPort instead.
It seems to be a bit of a gamble whether you get SBUS or SmartPort, it might be firmware-dependent.
On firmware 2.1.0 FPort, I actually got the uninverted FPort signal on the CPPM pin, which is what I wanted.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on November 24, 2020. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
