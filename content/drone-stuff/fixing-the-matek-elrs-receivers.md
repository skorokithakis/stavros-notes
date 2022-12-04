# Fixing the Matek ELRS receivers

The Matek ELRS receivers (ELRS-R24-D, ELRS-R24-S, etc) are dangerously close to out of spec, [due to the addition of two XTAL capacitors](https://docs.google.com/document/u/1/d/10m25KMzpuve8kn1ToP7wEt3qKzD9NwbL6vCAcM_DwCs/mobilebasic). The Semtech chip Matek is using for the receiver already contains XTAL capacitors in it, so the two added capacitors are redundant and push the frequency close to the edge of the spec. This means that temperature changes might push the frequency off-spec, and cause a failsafe randomly in mid-air.

The Matek receivers with a silver boot button are more prone to the issue, but it's also present in newer batches with gold boot buttons.

Luckily, this issue is easy to fix (and the fix is the same for both batches). You just need to desolder/remove the two capacitors shown below:

![d8d349e62a17404996ff64a377687bf3.png](/resources/8eff90fdedb94cd7b8d9237f948b388c.png)

* * *

<p style="font-size:80%; font-style: italic">
Last updated on December 04, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
