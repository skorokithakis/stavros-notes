# Macropad build

# Macropad build

Custom macropad project based on void16 redux.

## Log

- 2025-12-30: Project started
- 2025-12-30: Printed void16 redux version from https://github.com/victorlucachi/void16
- 2022-12-30: Printed red keycaps
- 2025-12-30: Hand-wired/soldered the build
- 2025-12-30: Used nice!nano clone with ZMK and a small battery
- 2025-12-30: Attempting to build ZMK locally
- 2025-12-30: Works!
- 2025-12-30: Connection stability issue - macropad disconnects/reconnects every few minutes. Conditions: device was charging, bluetooth headphones were also connected. Investigating.
- 2025-12-30: Changed keymap from F13-F24 keys to regular keys with Ctrl+Shift+Super modifier. F-keys were triggering system actions (e.g., Alt+F20 mutes mic in GNOME). New layout: numbers (layer 0), QWERTY top row (layer 1), home row (layer 2), bottom row (layer 3). Removed Alt from modifier to avoid Alt+Shift triggering language switch.
- 2025-12-30: Added combo to switch to bootloader.
- 2025-12-30: Added combo to clear Bluetooth pairings (long-press all 4 layer buttons).
- 2025-12-31: Switched from left control to right control for the modifier combo, to avoid conflicts with left-ctrl shortcuts.
- 2025-12-31: Expanded from 4 layers to 15 layers using button combinations. Single buttons for layers 0-3, multiple simultaneous buttons for layers 4-14.
- 2025-12-31: Added gaming layer (layer 12, activated by buttons 0+2+3) with WASD layout, ESC/TAB/CTRL on left column, ALT/Enter/Space on bottom row.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 31, 2025. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
