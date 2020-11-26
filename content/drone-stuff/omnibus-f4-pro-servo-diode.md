+++
title = "Omnibus F4 pro servo diode"
weight = 3
sort_by = "weight"
insert_anchor_links = "right"
+++
To isolate the servo 5V rail from the controller's 5V power supply, remove this diode:

[![a435bcae86912205b6fac41731285b8d.png](../../resources/6d668e05d8a54580966b94a752f3b7db.png)](../../resources/6d668e05d8a54580966b94a752f3b7db.png)

Now the servos' 5V rail can be powered from another 5V supply to avoid servo current backflow into the FC.