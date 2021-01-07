+++
title = "A simple guide to PID control"
weight = 1
sort_by = "weight"
insert_anchor_links = "right"
+++
I made some changes to my quadcopter the other day for [a new photography project I'm working on](https://www.makerfol.io/project/m8xrLUp-light-painting-with-drones/).
Unfortunately, it turned out that it wasn't good enough, and that I'd have to tune my [PID loop](https://en.wikipedia.org/wiki/PID_controller), which I knew nothing about.
After watching a few videos and reading a few things, I learnt enough to be dangerous, and to hopefully be able to explain the concepts simply, so I want to write them down here before I forget.

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
Last updated on January 07, 2021.  For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
