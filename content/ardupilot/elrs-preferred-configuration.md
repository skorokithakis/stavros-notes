# ELRS preferred configuration

If you have an ExpressLRS system, this is my preferred config for ELRS 3.x:

## Packet rate

**100 Hz Full**

As I fly long-range fixed-wing, I go for *100 Hz Full* to get range and telemetry bandwidth.

## Telemetry ratio

**1:2**

I use this to get a high telemetry rate. It could probably go lower, but I don't think it hurts anything.

## Switch mode

**12ch Mixed**

I use this mode because I prefer having full rate on channels 1-4, rather than have three extra channels. For details, see [the documentation](https://www.expresslrs.org/3.0/software/switch-config/).

## TX Power

**Dynamic power at 250 mW max.**

I use this because dynamic power works well enough, and my transmitter only does 250 mW max. If yours does more, feel free to set it to that.

## Model match

**Off**

I don't like model match, as I have one radio model for all my ELRS planes. Having model match enabled would mean that I need one radio model per plane.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on November 19, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
