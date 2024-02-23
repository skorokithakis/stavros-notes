# Cloning cards/fobs with a Proxmark3

## Cloning a Paxton fob

Basically, follow this guide:

https://badcfe.org/how-to-paxton-with-proxmark/

I managed to read my fob with:

```
lf hitag read --ht2 -k BDF5E846
```

If you're getting "Password failed!" or nothing back, move the fob around the 125KHz antenna (the top one), it should eventually work.

Afterwards, [convert the fob pages to an EM4100 ID](https://static.badcfe.org/paxton-covert), and flash the ID to a T5577, emulating an EM4100 chip:

```
lf em 410x clone --id <your hex id>
```

Read it back to make sure:

```
lf em 410x reader
```

You should be done, but I haven't tested it as I don't have a Paxton reader handy.

### Related reading

* [Iceman's Proxmark3 firmware (use this one)](https://github.com/RfidResearchGroup/proxmark3)
* [How to copy Paxton fobs using an RFIDler](https://gist.github.com/natmchugh/18e82761dbce52fa284c87c190dc926f#getting-hold-of-hitag2-tags)
* [ How to copy, read and write Paxton fobs and cards with a Proxmark ](https://badcfe.org/how-to-paxton-with-proxmark/)

## Cloning MiFare cards

See [Cloning a Mifare Classic 1K](https://www.gavinjl.me/proxmark-3-cloning-a-mifare-classic-1k/).

## Card cloner

I have an AliExpress cloner which clones LF cards. Unfortunately, whenever it clones a card, it sets the password bit on it. To remove it with the Proxmark3, run:

```
lf t55 wipe --p 51243648
```


* * *

<p style="font-size:80%; font-style: italic">
Last updated on February 24, 2024. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
