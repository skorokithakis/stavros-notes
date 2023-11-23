# Notes on my TimSav

A few years ago I made a TimSav foam cutter CNC. These are my notes on it, because I keep forgetting things.

* It runs [FluidNC](https://github.com/bdring/FluidNC).
* `M3 S200` enables the spindle at 20%, `M3 S0`/`S0` disables it, `M5` halts it.

To generate the Gcode, I use a program called [LaserWeb](https://laserweb.yurl.ch/). I have a few notes on it:

* After you load an SVG, you need to click the leftmost button below the SVG, with the three cubes. This will select all the paths to generate movements for.
* You need to click "Create single" to create a path to mill.
* I use "Laser Cut" as the tool.

I created a small script, `cnc_unwanted_moves`, to remove unwanted tool off/on at each corner. I won't share it here, as it's too specific to my configuration, and probably useless to anyone else.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on October 02, 2023. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
