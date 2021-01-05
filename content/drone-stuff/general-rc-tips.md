+++
title = "General RC tips"
weight = 0
sort_by = "weight"
insert_anchor_links = "right"
+++
These are general tips for building RC planes/quads/whatever:

* Propellers have a direction: The top usually has letters like, for example, "6040" (which denotes the size and pitch of the propeller), and the top needs to always point towards where the plane will be flying (the front). No matter if you have a pusher or puller, the top of the propeller needs to be pointing forward.
* When it comes to cameras/standards, the difference between PAL and NTSC is that PAL has higher resolution (625 lines, ie 576i for PAL vs 525 lines, ie 480i for NTSC), but lower framerate (25 fps for PAL vs 29.97 fps for NTSC). I use PAL because I prefer having higher resolution.
* If doing manual/hand launches of planes/wings, you'll notice that you need to have your hand on the pitch/roll stick when launching, which means you need to launch with your left hand, which is where the arm and throttle controls usually are. That makes it hard to throttle up to start the launch, or down (or disarm) in an emergency.

  To make things a bit easier, I set the back right switch (SG) to override the throttle and set it to the launch throttle (40% for me, for example). That way, I can arm, keep the throttle down, and flip SG with my right hand. That will throttle up enough to easily launch the wing, and if something goes wrong I can still either disarm or flip SG down so the motor stops again.


## PID controller

Basically, a PID loop can be thought of very simply as an equation that takes your current state as input and gives you what you need to do to reach a desired state as output.
For example, if you had a radiator and wanted to heat a room, the PID loop would take the current temperature as input and tell you how high you needed to set the radiator on a 0-100% scale to achieve a desired temperature.

The PID loop has three components, and to tune it you need to set three weights that you multiply each parameter with.
That means that it's basically `output = P*prop, + I*intgr + D*deriv`, where the terms are explained below:

* **`P` - proportional**: This is the weight of the difference between the current position and the desired position.
  What this says about the radiator is "we're still far away, we need more heat!", so the more P you set, the higher the radiator will be set for a given temperature difference.
* **`D` - derivative**: Because `P` is purely based on the difference between the current and target temperatures, it doesn't know anything about inertia.
  So, even though your radiator will be getting closer to the target temperature, even when it's very close, P will be saying "more heat, we're not there yet!", and cause you to overshoot your target, having to then go back (possibly turning the AC on, undershooting downwards, and then back upwards, oscillating like that for a long time).
  D helps by saying "whoa, we're getting there, slow down with the heat", and reducing the amount of heat you apply proportionally to how fast you're getting to your target temperature.
* **`I` - integral**: `I` helps in the case where you left a window open in the room, and `P` is saying "okay we're pretty close so set the radiator to 10% just for that final push", but the room is leaking so that 10% will never get you to your target temperature.
  `I` helps by saying "Okay we've been trying but it's not working, we're still far, so we actually need a bit more heat than 10%", by looking at the constant temperature difference you've been having lately, despite your best efforts.
  Basically, `I` deals with accumulated error when you think you're getting closer but all you're doing is fighting losses, so `I` allows you to close that gap.

That's pretty much it!

* * *

<p style="font-size:80%; font-style: italic">
Last updated on January 05, 2021.  For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
