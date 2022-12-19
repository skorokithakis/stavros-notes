# Battery discharge curves

I wanted to buy some Sony VTC6 batteries, and I was wary of fakes, so I wrote a [battery discharge calculator](https://gitlab.com/stavros/assault-and-battery/) with an associated hardware component (just a simple current and voltage sensor). I then took some measurements of my known-good batteries, and the new ones I bought.

The methodology was the following: I connected the battery to the sensor, and the sensor to a configurable load. I set the load to draw a certain amount of amps until it reached a cutoff voltage, and then to stop. I then plotted mAh drawn versus voltage, as well as amps drawn.

The batteries I connected were in various states of use, and various configurations (for various reasons, I couldn't test single cells). The configuration, state of the battery and provenance are mentioned below.

Here are the graphs:


## Genuine Sony VTC6

This is a genuine (as far as I can tell) Sony VTC6, fairly used in high amp draw situations (I use it in my plane), in a 3S configuration:

![curve_old-3s_2021-09-08_02-53-53.png](/resources/71aaa540c06d48e59559d05627ceffa4.png)

You can see that it output around 2600 mAh before I stopped it at 3V, which is quite good.

Here's a brand new genuine VTC6, again in a 3S configuration:

![curve_new-vtc6-3s_2021-09-09_13-06-52.png](/resources/9a2ed9fc5d474edfab2ec610e994c059.png)

This time I ran it all the way down to 2.8, and you can see it output the full 3000 mAh.


## Fake Sony VTC6

This is a pretty blatantly fake "Sony VTC6", brand new, in a 2S configuration:

![curve_new-vtc6_2021-09-08_18-54-58.png](/resources/2d20e92b9b2247e39de7458e0b341d45.png)

The performance falls off a cliff after around 3.6V, and it only outputs 1600 mAh before it dies completely.

Trying to draw 6-7A is even more spectacular (and it gets very hot to the touch):

![curve_new-vtc6-6a_2021-09-08_23-57-29.png](/resources/b3a7a012f9d5418e9e2e9867fd23df61.png)

Notice the huge voltage sag right as the load starts drawing.

## Reclaimed NKON VTC-6

I bought some [reclaimed Sony VTC-6 from NKON.nl](https://www.nkon.nl/sony-us18650-vtc6-reclaimed.html), and I tested them here, in a 2S configuration at 1.5A.

They seem to be very genuine:

![curve_reclaimed_NKON_VTC-6_2S_1.5A_2022-12-19_14-50-18.png](/resources/55e13b1a5b5142219d655504448e5b02.png)

Not only are they genuine, but if we compare with the graph of the brand new VTC-6 above, we see that the reclaimed NKON batteries have had zero (or very few) cycles, as they gave the same Ah at 3.3V/cell as the new ones.


If you need it, here is the [raw Assault and Battery CSV](/resources/29e39ead4d104c2c8133b028882b6a98.csv).


## White CNHL 4S 4000 mAh

This is a white CNHL 4S 4000 mAh LiPo battery, slightly used:

![curve_cnhl-4ah-used_2021-09-11_20-29-53.png](/resources/ba59455ecc2946fd8b2f001dfa32378a.png)

You can see that it's pretty decent, outputting nearly all of its nominal mAh, decently linearly, with a slightly faster drop after 3.7 V.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 19, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
