+++
title = "Battery discharge curves"
weight = 1
sort_by = "weight"
insert_anchor_links = "right"
+++
I wanted to buy some Sony VTC6 batteries, and I was wary of fakes, so I wrote a [battery discharge calculator](https://gitlab.com/stavros/assault-and-battery/) with an associated hardware component (just a simple current and voltage sensor). I then took some measurements of my known-good batteries, and the new ones I bought.

The methodology was the following: I connected the battery to the sensor, and the sensor to a configurable load. I set the load to draw a certain amount of amps until it reached a cutoff voltage, and then to stop. I then plotted mAh drawn versus voltage, as well as amps drawn.

The batteries I connected were in various states of use, and various configurations (for various reasons, I couldn't test single cells). The configuration, state of the battery and provenance are mentioned below.

Here are the graphs:

## Genuine Sony VTC6

This is a genuine (as far as I can tell) Sony VTC6, fairly used in high amp draw situations (I use it in my plane), in a 3S configuration:

![curve_old-3s_2021-09-08_02-53-53.png](../../resources/71aaa540c06d48e59559d05627ceffa4.png)

You can see that it output around 2600 mAh before I stopped it at 3V, which is quite good.

Here's a brand new genuine VTC6, again in a 3S configuration:

![curve_new-vtc6-3s_2021-09-09_13-06-52.png](../../resources/9a2ed9fc5d474edfab2ec610e994c059.png)

This time I ran it all the way down to 2.8, and you can see it output the full 3000 mAh.


## Fake Sony VTC6

This is a pretty blatantly fake "Sony VTC6", brand new, in a 2S configuration:

![curve_new-vtc6_2021-09-08_18-54-58.png](../../resources/2d20e92b9b2247e39de7458e0b341d45.png)

The performance falls off a cliff after around 3.6V, and it only outputs 1600 mAh before it dies completely.

Trying to draw 6-7A is even more spectacular (and it gets very hot to the touch):

![curve_new-vtc6-6a_2021-09-08_23-57-29.png](../../resources/b3a7a012f9d5418e9e2e9867fd23df61.png)

Notice the huge voltage sag right as the load starts drawing.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 09, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
