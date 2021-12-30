# Black pills

I've been trying to flash these Black Pills I have (STM32F401), the official STM32 flasher worked great, [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html).

Run with:

`./STM32_Programmer.sh -c port=USB1 -d firmware.bin 0x08000000`

 `dfu-util` also worked, eventually, after an unspecified amount of messing around with udev rules (if it doesn't work for you out of the box, try the rs-probe udev rules).
 
 
## Useful links

* https://therealprof.github.io/blog/usb-c-pill-part1/
* https://blog.tonari.no/rust-simple-hardware-project
* https://github.com/stm32-rs/stm32f4xx-hal


## This finally worked

Clone the repo: https://github.com/stm32-rs/stm32f4xx-hal/ and `cd examples`.

`cargo objcopy --release --example delay-timer-blinky --features="stm32f401,rt" -- -O binary out.bin`

`dfu-util -a 0 --dfuse-address 0x08000000 -D out.bin`

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 30, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
