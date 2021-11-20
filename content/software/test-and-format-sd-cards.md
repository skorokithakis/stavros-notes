# Test and format SD cards

I wrote a short bash script that tests SD cards with [F3](https://3ds.hacks.guide/f3-(linux).html) to see if they're fake, deletes everything on them, creates a new partition table and one exFAT partition on them.

Here it is:

```bash
#!/usr/bin/env bash

set -euox pipefail

sudo umount --force "$1"1 || true
sudo f3probe --destructive --time-ops "$1"
sudo parted --script "$1" "mklabel msdos" "mkpart primary ext4 0% 100%"
sleep 1
sudo mkfs.exfat -n Stavros "$1"1
eject "$1"
```

Save it as `formatsd.sh` and run it as `./formatsd.sh /dev/sdX`.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on August 18, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
