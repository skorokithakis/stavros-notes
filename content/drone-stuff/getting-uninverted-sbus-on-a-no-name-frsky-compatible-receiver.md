# Getting uninverted SBUS on a no-name FrSky-compatible receiver

I got an [RC receiver](https://www.banggood.com/2_4G-8CH-D8-Mini-FrSky-Compatibel-Receiver-With-PWM-PPM-SBUS-Output-p-1140478.html?rmmds=myorder&cur_warehouse=CN) from Banggood. 

To bind, hold the button down while plugging in the power. When the LED is solid blue, you've bound. To get PWM out of its channels, desolder both PPM/SBUS bridges (or, at least, I *think* this is necessary).

![bea490ccc458840c97c9b4d0dac29c22.png](/resources/3ab56ddd639a4147bf34fde0222bcbe0.png)

![c7757324e7db0b41d5e578dfe444506d.png](/resources/6e72628402cf42af837d1b4942710de8.png)

There's uninverted SBUS on this pad:

[![rc-sbus.jpg](/resources/ccc7571db5d147328860077fdc0aa745.jpg)](/resources/ccc7571db5d147328860077fdc0aa745.jpg)

To break this out to the SBUS pad, I had to remove/bridge the resistor that is circled in the image, and remove/bridge the FET on the other side:

[![rc-sbus-mosfet.jpg](/resources/1b0f508a533e45b496c6636d49161b0c.jpg)](/resources/1b0f508a533e45b496c6636d49161b0c.jpg)



* * *

<p style="font-size:80%; font-style: italic">
Last updated on April 17, 2026. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
