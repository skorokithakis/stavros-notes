# Pairing the Xbox One controller in Linux

Sometimes, the Xbox One controller won't pair in Linux, instead connecting and disconnecting rapidly. To fix that:

* Install [xone](https://github.com/medusalix/xone).
* Disable ERTM:
   `echo 'Y' | sudo tee /sys/module/bluetooth/parameters/disable_ertm`
* Pair!

That should be all that's required, your controller should now be paired.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on July 14, 2023. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
