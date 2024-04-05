# Details about my Sapphire Pro

My Sapphire Pro runs the MKS Robin Nano 1.2 board. Details on that board (pinouts, diagrams, etc) are here:

[https://github.com/makerbase-mks/MKS-Robin-Nano-V1.X/wiki/Wiring_Pinout_and_Size](https://github.com/makerbase-mks/MKS-Robin-Nano-V1.X/wiki/Wiring_Pinout_and_Size
)

## TMC2209 drivers

I've installed TMC2209 drivers and wired all their UARTs up to the same pin, PA13, as recommended [in this GitHub issue](https://github.com/Klipper3d/klipper/issues/4779). Their addresses for X, Y, Z, and E are 0, 1, 2, and 3, respectively. It doesn't work with Klipper, I'm only getting the error message `TMC stepper_x failed to init: Unable to read tmc uart 'stepper_x' register IFCNT`. Nothing I've tried has worked, the last resort is setting the baud rate to 19200. If you managed to make this work, please email me.

## SFS 2.0 filament motion runout sensor

I've installed the SFS 2.0 motion runout sensor on MT_DET1 and MT_DET2. This means that the motion sensor pin is PE6, and the switch sensor is PA4. That doesn't work either, Marlin keeps thinking the printer has run out of filament.

https://github.com/MarlinFirmware/Marlin/issues/26916

* * *

<p style="font-size:80%; font-style: italic">
Last updated on April 05, 2024. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
