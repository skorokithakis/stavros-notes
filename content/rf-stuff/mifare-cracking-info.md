# MIFARE cracking info

From [kweks on HN](https://news.ycombinator.com/item?id=41599584):

There are multiple ways to crack MIFARE - depending on the actual chipset version / manufacturer.
For Mifare Classic: - Nested (Uses one known key to crack others) - darkside (Derives a key with no others. Slower, results are typically handed off to the nested attack to calculate remaining keys..)

For newer versions of the Mifare Classic with better PRNGs - "Hardened" cards: HardNested. Needs one known key.

For cards that provide a static nonce (to try to evade cracking, ie FUDAN) - Static Nested.

For the latest generation FUDAN: Static Encrypted HardNested.

Note, for the nested attacks - if you don't have a known key, these can be sniffed from the access control reader, and then cracked (MFKey32/64).

Flipper supports the MFKey32 attacks, and limited nested. You may bump into limits of your Proxmark clone with hardnested cracking - it's memory intensive, and most of the Proxmark Easy clones have reduced RAM.

There's actually an auto_crack LUA script on proxmark ( Use this fork: https://github.com/RfidResearchGroup/proxmark3 ) which will take most of the hassle out of cracking.

Cracking requires very, very precise timing: In a nutshell, you're trying to predict nonces / PRNG values, by sending very precicesly timed requests, and then later cracking those results.

The Flipper has limited CPU power - its main "attack vector" against MIFARE is a very large keylist / dictionary of common MIFARE keys. It's slow and dumb, but it works for most cases. It can also do limited cracking, depending on the type required.

The Proxmark is built around an FPGA, and can crack much, much more efficiently.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 20, 2024. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
