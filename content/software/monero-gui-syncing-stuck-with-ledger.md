+++
title = "Monero GUI syncing stuck with Ledger"
weight = 1
sort_by = "weight"
insert_anchor_links = "right"
+++
This is about the Monero desktop GUI, but probably also applies to Monerujo.

If you're trying to sync the blockchain with your Ledger device, you might be getting the conflicting messages of "Waiting for daemon to sync" and "Daemon is synchronized", which then just stays there forever and doesn't move.

You may see something like this in the log:
```
ERROR	wallet.wallet2	src/wallet/wallet2.cpp:3449	Error parsing blocks: Unable to send hidapi command. Error 128: Unknown error
ERROR	wallet.wallet2	src/wallet/wallet2.cpp:3512	pull_blocks failed, try_count=3
```

These errors are caused by the Ledger not being connected. You need to leave the Ledger connected throughout the syncing, as apparently the node needs some info from it and won't notify you if it's not there. It also doesn't seem to work if you disconnect and then connect the wallet afterwards.

Letting the Ledger go to the screen saver or lock appears safe, at least with the Nano X I tried. Just leave it connected, and it'll sync fine.

I've opened a suggestion on the [Monero issue tracker](https://github.com/monero-project/monero/issues/7276) to improve the UX of the Ledger integration in general.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on January 04, 2021.  For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
