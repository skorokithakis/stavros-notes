+++
title = "Omnibus F4 pro servo diode"
weight = 11
sort_by = "weight"
insert_anchor_links = "right"
+++
To isolate the servo 5V rail from the controller's 5V power supply, remove this diode:

[![a435bcae86912205b6fac41731285b8d.png](../../resources/6d668e05d8a54580966b94a752f3b7db.png)](../../resources/6d668e05d8a54580966b94a752f3b7db.png)

Now the servos' 5V rail can be powered from another 5V supply to avoid servo current backflow into the FC.

There's also a 	[schematic for this FC](../../resources/805930c3bedc4393ba947f0e0bfa369d.pdf).

* * *

<p style="font-size:80%; font-style: italic">
Last updated on April 09, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
