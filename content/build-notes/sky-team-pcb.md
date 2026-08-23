# Sky Team PCB

**Project:** A physical electronics/PCB interface for the cooperative two-player board game Sky Team, built with Nicolas Mattia.

## Details

Sky Team is a silent co-op landing game: Pilot and Co-pilot secretly roll dice, then alternate placing them on a shared cockpit panel to manage the aircraft’s axis, engines/speed, radio/traffic, flaps, landing gear and brakes. The silence during placement is central to the game, so any augmentation must preserve that constraint.

### Physical game interface
- The core is a triple-layer control panel with an airplane-axis disc, coloured dice spaces, tracks/markers, and 10 physical switches.
- The switches belong to the **flaps**, **landing gear**, and **brakes** systems; gear and flaps expose green status lights when deployed.
- Flaps and landing gear affect the two aerodynamics markers; brakes are relevant to the final landing speed.
- Axis and engines are mandatory dice placements every round.
- The game has 11 airports and 21 scenarios, with extra modules such as wind, kerosene, ice brakes and an intern.

### PCB scope
Initial scope is to understand the existing control-panel mechanisms and decide what the electronics should sense, illuminate, or control. Software is deliberately later. Do not assume the board’s switches/LEDs share a simple circuit: map and test the real behaviour first.

### Open technical question
Some switches appear to reveal/activate their corresponding green indicators, while other indicators represent counters. Test whether an input can drive an LED suitably, including the proposed switch-in-series arrangement, before choosing the interface circuit.

### Next steps
- Nicolas to acquire and play the game, then jointly identify the useful interactions to augment.
- Inspect and map the panel’s switches, lights, disc and any relevant connections.
- Test the LED/switch/input behaviour with real hardware.
- Define the PCB interface and only then consider software.

## Resources

- [Official Sky Team page](https://www.scorpionmasque.com/en/sky-team) - publisher overview, components and scenarios
- [Sky Team on BoardGameGeek](https://boardgamegeek.com/boardgame/373106/sky-team) - game reference
- [Project discussion thread](https://discord.com/channels/1303124786498637834/1540811780790558912) - Discord thread

## Log

- **2026-08-22:** Stavros and Nicolas Mattia started the Sky Team PCB project. Nicolas planned to pick up the game in Zurich the following week and play it before brainstorming. Agreed to prioritise working out the physical connections over software. Captured the open question around switches, LEDs and input drive for hardware testing.
- **2026-08-23:** Reviewed the official game information and refined the project reference around the cockpit panel, its 10 switches, the silent dice-placement constraint, and the need to preserve the game’s interaction model.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on August 23, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
