# Sleight of hand

**Project:** ESP32-driven analog wall clock - replace the timing IC and drive the coil directly from GPIO, enabling custom movement modes.

**Repo:** https://github.com/skorokithakis/sleight-of-hand

## Details

- ESP32-C3 SuperMini (esp32-c3-devkitm-1 board definition)
- Cheap no-name sweeping quartz wall clock with timing IC removed
- GPIO 4 → Coil pin A, GPIO 5 → Coil pin B
- Coil resistance: 600 ohm
- 820 ohm series resistor on one coil pin (delivers 2.32 mA at 3.3V)
- **960 pulses per revolution** (measured: 5761 pulses over 6 revolutions = 960.17)
- Original IC drives at ~62.5ms per cycle (31.25ms pulse + 31.25ms pause)
- WiFi AP name: SleightOfHand
- Three movements purchased total: two sweeping, one ticking

### Key discovery: it's a sweeping clock

- This is a sweeping-motion clock, not a ticking clock. The original IC drives continuous sweeping pulses (~30ms pulse, ~30ms pause), not one-pulse-per-second.
- All initial debugging failures were because the firmware was driving one pulse per second (ticking mode), which is the wrong drive mode entirely.
- Confirmed by buying a second identical clock, testing with battery first, and analyzing the original PCB with multimeter and oscilloscope.

### Motor drive

- ESP32-C3 GPIO default drive strength is 40mA, much more than needed. Can reduce with `gpio_set_drive_capability()` (5/10/20/40mA). Using `GPIO_DRIVE_CAP_0`.
- Tested timing limits: pulses down to 15ms (pulse and pause) work reliably. 10ms and below fail.
- Firmware uses 960-pulse model anchored to NTP minute boundaries. Two modes: steady (62ms cycle) and rush_wait (50ms cycle, ~12s idle at end of minute).

### Power delivery

- Original battery: 1.5V across 600 ohm = 2.5 mA, 3.75 mW
- At 3.3V with no series resistor: only ~5.5 mA
- To match original 2.5 mA at 3.3V: need 1320 ohm total → 680-750 ohm series resistor
- Final: 820 ohm series resistor → 2.32 mA, slightly under original but works perfectly

### Ticking movement

- Experimenting with a 150 Ω series resistor to lower tick strength
- Still tuning the resistor value

### Communication

- MQTT control commands: stop, start, start_at_minute (waits for NTP minute boundary)
- MQTT reconnect only attempted during idle gap between revolutions to avoid stalling pulses
- UDP broadcast logging on port 37243 for wireless debugging (`nc -kul 37243`)

### Build notes

- Serial output on SuperMini requires USB CDC flags: `-DARDUINO_USB_MODE=1 -DARDUINO_USB_CDC_ON_BOOT=1`
- Original driver PCB was desoldered and removed
- Idle state between pulses: high-impedance (`pinMode(..., INPUT)`)

## Log

- **2026-02-10:** Project initialized with PlatformIO (ESP32 Arduino framework). Basic coil driver written, repo created on GitHub. Switched board to ESP32-C3 SuperMini.
- **2026-02-11:** Switched coil pins to GPIO 4 and 5. Removed series resistors. Extensive debugging - rotor flails/oscillates instead of making clean steps. Tested pulse widths 5-200ms, various drive strengths, both polarities. Tried short-brake after drive pulse. Measured coil at 600 ohm.
- **2026-02-12:** Bought a second identical clock and tested with battery first - discovered it's a sweeping clock, not ticking. Retrieved original PCB from trash, confirmed sweeping drive on oscilloscope.
- **2026-02-12:** Updated firmware to 30ms pulse / 30ms pause continuous drive. Installed 820 ohm series resistor. Clock works perfectly.
- **2026-02-12:** Measured 960 pulses/revolution. Rewrote firmware to NTP-anchored 960-pulse model with steady and rush_wait modes.
- **2026-02-12:** Added MQTT control and UDP broadcast logging. Done and working.
- **2026-02-23:** Working on adding ticking movement support. Debugging an off-by-one error in the ticking timing code - hard to pin down.
- **2026-02-24:** Experimenting with a 150 Ω series resistor to reduce tick strength on the ticking movement. Still tuning.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 24, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
