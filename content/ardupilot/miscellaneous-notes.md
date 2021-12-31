# Miscellaneous notes

These are random AP-related notes that wouldn't fit anywhere else:

## DMA on the Matek F405-Wing

If you want to get DMA on UART3 of the Matek F405-Wing FC (or, more relatedly, the Racerstar F405, because UART1 is Bluetooth there), you can open `libraries/AP_HAL_ChibiOS/hwdef/MatekF405-Wing/hwdef.dat` and comment out line 92ish, where PA15 is defined.

That will enable DMA on UART3, at the expense of disabling the LED pad.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 31, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
