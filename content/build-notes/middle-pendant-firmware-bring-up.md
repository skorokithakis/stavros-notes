# Middle pendant firmware bring-up

**Project:** Voice recorder pendant - ESP32-S3 wearable with BLE sync, MP3 recording, and GPT-4o transcription.

## Details

- ESP32-S3 SuperMini
- PlatformIO project, target: esp32-s3-devkitc-1
- Button pin: GPIO12
- BLE sync protocol with Python client
- BLE stream chunk size: 20 bytes (matching observed MTU 23)
- Records MP3, syncs via BLE, transcribes with GPT-4o to .txt files
- BLE advertising starts after successful recording and on boot when pending files exist
- ESP32-S3 ADC pins: ADC1 (GPIO 1-10) works with WiFi active, ADC2 (GPIO 11-20) not available when WiFi is in use. 20 channels total, 12-bit resolution (0-4095, 0-3.3V). S3 has better hardware calibration than old ESP32 - stick to ADC1 if using WiFi.

## Log

- **2026-02-15:** Initialized PlatformIO project for ESP32-S3. Implemented initial firmware and BLE sync protocol scaffolding. Added Python sync client with BLE transfer flow.
- **2026-02-15:** Resolved board mismatch by switching to esp32-s3-devkitc-1 with USB mode adjustments. Ran staged firmware restore to isolate issues.
- **2026-02-15:** Confirmed button pin as GPIO12. Switched BLE chunk size to 20 bytes for MTU 23 compatibility.
- **2026-02-15:** Added ACK/SYNC handling hardening. Updated sync client to save MP3 and added GPT-4o transcription.
- **2026-02-15:** Updated firmware so BLE advertising starts after recording and on boot with pending files. Fixed repeated file transfer behavior with delete-path normalization.
- **2026-02-18:** Made a 3D printed case for the pendant - should be usable now.
- **2026-02-22:** Installed a new digital microphone on the pendant.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 23, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
