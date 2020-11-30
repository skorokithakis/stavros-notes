+++
title = "Getting uninverted SBUS/SmartPort on the FrSky XSR receiver"
weight = 2
sort_by = "weight"
insert_anchor_links = "right"
+++
To get uninverted SBUS/SmartPort on the FrSky XSR/X4RS receiver, you can repurpose the CPPM pad.
Remove the two small resistors shown in the image, and solder the two lower pads (together) to either the CPPM pad or the MOSFET pin shown in the photo:

[![xsr-sbus.jpeg](../../resources/f86da9a7aac1413ebd77825897164f7f.jpeg)](../../resources/f86da9a7aac1413ebd77825897164f7f.jpeg)

They should be soldered like this (remember to solder both resistor pads together):

[![xsr-sbus2.jpeg](../../resources/815576429ece43789dbc70dfd33517a1.jpeg)](../../resources/815576429ece43789dbc70dfd33517a1.jpeg)

Now the CPPM pad will be uninverted SBUS/SmartPort instead.
It seems to be a bit of a gamble whether you get SBUS or SmartPort, it might be firmware-dependent.
On firmware 2.1.0 FPort, I actually got the uninverted FPort signal on the CPPM pin, which is what I wanted.

* * *

Last updated on 2020-11-24 04:21:44.
