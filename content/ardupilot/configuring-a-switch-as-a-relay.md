# Configuring a switch as a relay

If you want to connect a relay of some sort (something that accepts a low/high signal, like a camera control) to a PWM output (the servo outputs), you need to do a few quick things. The actual numbers will vary depending on your FC, but here's what worked for me with a Matek F405-Wing:

1. Set the channel you want the relay to trigger on as a controller for the first relay (here I'll assume you want to control the first relay on channel 11):  
  `RC11_OPTION=28`
2. Set the pin number for the relay you want to control. This is a bit fuzzy, it depends on your flight controller, but try a few out. This is what worked for me, for S6 on my F405-Wing:  
  `RELAY_PIN=55`
3. Set a servo to act as a GPIO output. I'm assuming here you want `SERVO6`, though I'm not quite sure how the servo selection maps to the `RELAY_PIN` selection above. For me, `AUXOUT6` and `SERVO6` worked:  
  `SERVO6_FUNCTION=-1`

If you're amazingly lucky, you should be all set. If not, you need to play with the `50` in the `RELAY_PIN` parameter and the `6` in the `SERVO6_FUNCTION` until something works.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 11, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
