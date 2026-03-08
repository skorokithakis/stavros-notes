# Macropad build

**Project:** Custom void16 redux macropad with nice!nano clone, ZMK firmware, and custom PCB.

## Details

- Based on [void16 redux](https://github.com/victorlucachi/void16)
- nice!nano clone microcontroller, ZMK firmware, small battery
- PCB designed in KiCad, fabricated at JLCPCB
- Keycaps: red for layer buttons (top row, 4 keys), black for the rest (12 keys) - printed from [flat MX keycap model](https://www.printables.com/model/67474-flat-mx-keycap)
- 15 layers via button combinations: single buttons for layers 0-3, multiple simultaneous buttons for layers 4-14
- Modifier: Right Ctrl+Shift+Super (switched from left ctrl to avoid shortcut conflicts, removed Alt to avoid triggering language switch)
- Gaming layer (layer 12, buttons 0+2+3): WASD layout, ESC/TAB/CTRL on left column, ALT/Enter/Space on bottom row
- Combo to clear Bluetooth pairings: long-press all 4 layer buttons

### PCB pin mapping

- Row 0: P0.02, Row 1: P1.15, Row 2: P0.10, Row 3: P1.11
- Col 0: P1.13, Col 1: P0.09, Col 2: P0.24, Col 3: P1.06
- Diode direction: col2row
- Footprint issue: one pin didn't exist on nice!nano (wrong KiCad footprint), hand-wired to P1.06
- Silkscreen error: +/- labels for battery connector are reversed

### Flashing

- Flash bootloader onto fake nice!nano boards using adafruit-nrfutil via USB-C ([troubleshooting guide](https://nicekeyboards.com/docs/nice-nano/troubleshooting/))
- Enter USB mass storage mode for firmware flashing: double-tap the reset pin quickly

## Resources

- [void16 redux](https://github.com/victorlucachi/void16)
- [Macro pad guide (jweather)](https://jweather.github.io/macro.html)
- [Making a macro pad from scratch (MakerLuis)](https://www.makerluis.com/making-a-macro-pad-from-scratch/)
- [Video reference](https://www.youtube.com/watch?v=_bRvMNMAWvo)
- KiCad footprints: [nice-nano](https://github.com/bstiq/nice-nano-kicad), [ProMicro](https://github.com/Biacco42/ProMicroKiCad), [TheOneProMicro](https://github.com/Aleblazer/TheOneProMicro), [key-switches.pretty](https://github.com/siderakb/key-switches.pretty)

## Log

- **2025-12-30:** Project started. Printed void16 redux case and red keycaps. Hand-wired and soldered the build with nice!nano clone, ZMK, and small battery. It works!
- **2025-12-30:** Connection stability issue - macropad disconnects/reconnects every few minutes while charging with Bluetooth headphones also connected. Investigating.
- **2025-12-30:** Changed keymap from F13-F24 to regular keys with Ctrl+Shift+Super modifier. F-keys were triggering system actions (e.g. Alt+F20 mutes mic in GNOME). Added combo to clear Bluetooth pairings.
- **2025-12-31:** Switched from left control to right control for modifier combo to avoid conflicts with left-ctrl shortcuts.
- **2025-12-31:** Expanded from 4 layers to 15 layers using button combinations. Added gaming layer (layer 12) with WASD layout.
- **2025-12-31:** Printing new keycaps - red for layer buttons, black for the rest.
- **2026-01-04:** Designed PCB in KiCad and sent to JLCPCB for fabrication.
- **2026-01-21:** PCBs arrived. Found footprint mistake - had to hand-wire one pin to P1.06. Also found silkscreen +/- reversal on battery connector.
- **2026-01-21:** Flashed bootloader onto fake nice!nano boards. Updated ZMK overlay with correct GPIO pins for PCB version.
- **2026-01-21:** 3D printed case refinements.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 23, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
