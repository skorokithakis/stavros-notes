# Getting VoWiFi working on Xiaomi.eu

I got a new Xiaomi phone (a Poco F4) and flashed it with Xiaomi.eu. Unfortunately, just like my Poco F3, Voice-over-WiFi wouldn't work. I had looked before, but I couldn't find anything, I assumed it was a problem with the phone. This time, I looked again, and found some posts hinting at it being a problem with the provisioning profile, and recommending using Qualcomm's QPST tool to load the MBN profile.

I tried that, but the profiles weren't there, or they wouldn't be enabled, and in general I just couldn't get it to work. Then, I came across [a post on the Xiaomi.eu forums](https://xiaomi.eu/community/threads/activation-of-volte-and-vowifi-in-xiaomi-eu-rom.63469/) that ended up working for me very easily, and I'm writing it up here in case I need it again.

## Enabling the profile

First, you should disable carrier checks for VoLTE and VoWiFi, just in case. You can do that by going to the dialer and entering the following number: `*#*#86583#*#*` (the numbers spell out "volte", which is easier to remember). Make sure the popup says "carrier check disabled", otherwise do it again until it does.

Then, do the same for `*#*#869434#*#*` (spells out "vowifi"), until that check is disabled too. Now you'll have the appropriate menus in the settings.

To actually load the profile, you need to enter the number `*#*#663368378#*#*` ("modemtest"). Then, go to "MBN config loading and activing tool" shown here:

![screen1.png](/resources/b7e313de59d4412382b2c36675085fdc.png)

Then press "Advanced":

![screen2.png](/resources/6489c6e219874e20a55fcb697dcd8ab3.png)

Select `mbn_eea.txt` (if you're in Europe), and then press "validate".

![screen3.png](/resources/f4679b76f438463382a2849083f6d51d.png)

 Wait for it to finish, then you should be set. Restart the phone, enable Airplane mode, enable WiFi and make a call. If it works, you're done.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on July 23, 2022. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
