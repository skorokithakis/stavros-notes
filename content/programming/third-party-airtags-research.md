# Third party AirTags research

It turns out you can buy some NRF51822 boards/tags on AliExpress (e.g. [this one](https://www.aliexpress.com/item/32826502025.html), but there are cheaper ones), and flash [a custom firmware](https://github.com/acalatrava/openhaystack-firmware) on them that will allow OpenHaystack integration, with the tags lasting years on a battery.

## Software
* https://github.com/acalatrava/openhaystack-firmware - The custom firmware.
* https://github.com/seemoo-lab/openhaystack/issues/57#issuecomment-880214651 - Some Ali boards don't have a crystal, but a crystal makes the tag last even longer.
* https://github.com/seemoo-lab/openhaystack/issues/35#issuecomment-828338751 - Instructions for building and flashing the firmware.
* https://github.com/dchristl/macless-haystack/ - An OpenHaystack server/client pair that allows you to track your tags from any browser.

## General info
* https://positive.security/blog/find-you - Details about how the anti-stalking features work (or don't).

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 28, 2024. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
