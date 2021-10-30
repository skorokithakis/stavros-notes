+++
title = "Building ArduPilot"
weight = 3
sort_by = "weight"
insert_anchor_links = "right"
+++
Because building ArduPilot is a bit complicated, I've written a short script that uses Docker to build AP in a controlled environment.

Copy it from here, save it to a file called `docker_build.sh` in the root of the ArduPilot repo, and run it with `docker_build.sh <your board>`. Output files will be stored in `build/<yourboard>/bin/`, and you can flash them with the [INAV configurator](https://github.com/iNavFlight/inav-configurator/releases) by putting your board in DFU mode and uploading the `arduplane_with_bl.hex` file.

Here's the script:

```bash
#!/usr/bin/env bash

set -euox pipefail

if [ $# -ne 1 ]
  then
    echo "No board supplied, run as ./docker_build.sh <board name> or ./docker_build.sh list"
    exit 1
fi

BOARD=$1

cd "$(git rev-parse --show-toplevel)"

git submodule update --init --recursive

git checkout Dockerfile
echo "RUN pip install intelhex" >> Dockerfile
echo 'ENV PATH="/home/ardupilot/.local/bin:/usr/lib/ccache:/ardupilot/Tools/autotest:${PATH}"' >> Dockerfile
cat Dockerfile

docker build . -t ardupilot
git checkout Dockerfile

# We need to update the PATH with the location of the ARM EABI inside the Docker
# container, so we write a script that handles this and the actual building.
cat <<EOF > undocker_build_temp.sh
#!/usr/bin/env bash

set -euox pipefail

export ARM_EABI=/opt/\$(ls -1 /opt/ | grep gcc-arm-none-eabi)/bin/
export PATH=\$ARM_EABI:\$PATH

./waf configure --board="\$1"
./waf build
EOF

chmod +x ./undocker_build_temp.sh

docker run --rm -it -v "$(pwd)":/ardupilot ardupilot ./undocker_build_temp.sh "$BOARD"

rm undocker_build_temp.sh
```

* * *

<p style="font-size:80%; font-style: italic">
Last updated on September 07, 2021. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
