+++
title = "GRBL_ESP32 tips"
weight = 2
sort_by = "weight"
insert_anchor_links = "right"
+++
I made a CNC that uses [a custom board I designed](https://gitlab.com/stavros/esp32-cnc), and which runs [GRBL_ESP32](https://github.com/bdring/Grbl_Esp32/). I couldn't find the following info easily, so I've written it here:

- You can specify the enable pin for the drivers with the `STEPPERS_DISABLE_PIN` option. This should be used like `#define STEPPERS_DISABLE_PIN GPIO_NUM_2`.
- To invert the enable signal, you can use `#define DEFAULT_INVERT_ST_ENABLE 1`. My board needed the enable signal to *not* be inverted (that's what A4988/Trinamic TMC2208 drivers need), so I set it to 0.
- To always keep the steppers enabled (locked) to avoid them moving, you can specify `$Stepper/IdleTime=255`. That's the maximum timeout and will always keep them enabled.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 15, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
