## MacOS
According to https://docs.docker.com/docker-for-mac/faqs docker for mac doesn't
support pass through for USB devices, so we have to use [Docker
Toolbox](https://docs.docker.com/toolbox/overview/#ready-to-get-started).
Download and install Docker Toolbox.

You'll also need the [Oracle VM VirtualBox Extension
Pack](https://www.virtualbox.org/wiki/Downloads). Note that you'll need to be
sure to have a compatible version of VirtualBox and the extension pack. If you
have an existing installation of virtualbox, you may need to update it.

First we create a virtual box VM to use
```
$ docker-machine create virtualbox
```

Then we stop it so we can configure it to enable USB ports
```
$ docker-machine stop virtualbox
```

Open up virtualbox, go to the VM named `virtualbox`, right click to open
settings. Go to Ports -> USB and enable the controller. Use the button
with the green plus to add the Lattice FTUSB Interface Cable.

Start the virtual machine again
```
$ docker-machine start virtualbox
```

It prompts us to use this command to see how to configure our shell
```
$ docker-machine env virtualbox
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/lenny/.docker/machine/machines/virtualbox"
export DOCKER_MACHINE_NAME="virtualbox"
# Run this command to configure your shell:
# eval $(docker-machine env virtualbox)
```

So we follow the instructions
```
$ eval $(docker-machine env virtualbox)
```

Now pull the image
```
docker pull lennyt/magma:latest
```

And run it
```
$ docker run -it --rm --device=/dev/ttyUSB0 --privileged lennyt/magma:latest /bin/bash
```

First, we can try compiling a simple test program using magma
```
(base) root@96cd16861daf:/# cd magmathon/tests
(base) root@96cd16861daf:/magmathon/tests# make
magma -b icestick -d "" blink.py
import lattice ice40
import lattice mantle40
compiling FullAdder
compiling Add22Cout
compiling Register22
compiling Counter22
compiling main
yosys -q -p 'synth_ice40 -top main -blif blink.blif' blink.v
arachne-pnr -q -d 1k -o blink.txt -p blink.pcf blink.blif
icepack blink.txt blink.bin
rm blink.v
```

Then, if you have an icestick, you can try uploading the test program.
```
(base) root@96cd16861daf:/magmathon/tests# make upload
iceprog blink.bin
init..
cdone: high
reset..
cdone: low
flash ID: 0x20 0xBA 0x16 0x10 0x00 0x00 0x23 0x51 0x73 0x10 0x23 0x00 0x35 0x00 0x35 0x06 0x06 0x15 0x43 0xB6
file size: 32220
erase 64kB sector at 0x000000..
programming..
reading..
VERIFY OK
cdone: high
Bye.
```

### Resources
* https://gist.github.com/stonehippo/e33750f185806924f1254349ea1a4e68
* http://gw.tnode.com/docker/docker-machine-with-usb-support-on-windows-macos/
