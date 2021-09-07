+++
title = "QGroundControl to Mission Planner conversion script"
weight = 11
sort_by = "weight"
insert_anchor_links = "right"
+++
If you have a parameter dump from QGroundControl, I wrote a small script that will convert it to a Mission Planner compatible file. You can also use [Parachute](https://gitlab.com/stavros/parachute) to do your backups/restores/conversions.

Just save this script somewhere as `convert_qgc_params` and run it as `./convert_qgc_params <qgc params> <output file>`:

```py
#!/usr/bin/env python3
import sys
from decimal import Decimal


def format_float(f):
    return "{0:f}".format(Decimal(f).quantize(Decimal("1.0000000")).normalize())


def main(infile, outfile):
    with open(infile) as ins:
        inputs = ins.read()

    lines = []
    for line in inputs.split("\n"):
        if not line or line.startswith("#"):
            continue
        vehicle_id, component_id, name, value, type = line.split("\t")
        v = value
        if type == "9":
            v = format_float(float(value))
        lines.append(f"{name},{v}\n")

    with open(outfile, "wt") as outs:
        outs.writelines(lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
```

* * *

<p style="font-size:80%; font-style: italic">
Last updated on March 04, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
