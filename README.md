Welcome to the homepage for the magmathon!

[Registration Form](https://goo.gl/forms/VkmP2Hs55ZnzHqRd2)

If you’d like to discuss project ideas, want to advertise a project in search of team members, or want to join an existing project, send us an email (lenny@cs.stanford.edu and hanrahan@cs.stanford.edu).

# Schedule
June 19th, 2018
```
 9:00am -  9:30am -- Setup and Installation
 9:30am - 10:00am -- Magma Tutorial (hello world)
10:00am - 10:30am -- Magma Assignment (signal generator)
10:30am - 11:30pm -- Magma In Depth (overview of language features)
11:30pm - 12:30pm -- Lunch
12:30pm -  4:30pm -- Freeform Hacking
 4:30pm -  5:00pm -- Show and Tell and Debrief
```

# Session Overviews

## Setup and Installation
All attendees will receive a Lattice ice stick to program and will have access to a basic lab environment with breadboards, wiring material and logic analyzers to use. Please get in touch with us early if you’d like to get any additional hardware (sensors, buttons, etc…) for your project and we can assist you. This session will be devoted to getting magma and other supporting software setup so you can program the Lattice ice stick.

## Magma Tutorial
This is a brief 30 minute session that will walk through creating a simple circuit in magma that blinks an LED on the Lattice ice stick. This simple introductory circuit is analogous to writing Hello World in a programming language, and introduces the fundamental concept of magma as well as demonstrating the integration with the open source synthesis tools used to program the FPGA.

## Magma Assignment
After our tutorial, we’ll provide a prompt for a circuit design that attendees can implement. This provides attendees a chance to integrate the material they learned in the tutorial to build their own magma circuit from scratch. The assignment will involve creating a signal generator on the FPGA, which can be used to drive a pattern using the on board LEDs or an audio output using a breakout board for a 3.5mm jack (bring headphones!). We’ll also show attendees how to use a logic analyzer to check and debug their designs.

## Magma In Depth
This hour long session will be a more in depth presentation of the magma language that focuses on features for building generators, meta programming, memories, testing, and simulation. The exact topics we cover will depend on the interest of the attendees, but the goal is to provide an in depth review of magma’s more complex features that will be useful for the hackathon projects.

## Freeform hacking
The afternoon will be devoted free form hacking where attendees are free to hack wherever they want. We’ll have lab space open for people who want to work with hardware materials. The goal of this hackathon is to support self organizing projects, so we’ll mainly be providing space, materials, and support for attendees. 

# Setup: Gettting Started with Magma and Mantle on the Icestick

We will be using Magma with the Lattice Icestick, a small FPGA with an
open-source tool chain.

![icestick](images/icestick.jpg)
> http://www.latticesemi.com/icestick
> USB thumb drive form factor evaluation board - [...] an easy to use, small size board that allows rapid prototyping of system functions at a very low cost using Lattice Semiconductor's iCE40 FPGA family.

### Icestorm tools

A major advantage of using this board is that all the tools needed to program
the FPGA are available as open source software that runs on Mac, Linux, and
Windows.

> http://www.clifford.at/icestorm/
> Project IceStorm reversed engineered and documented the bitstream format of
> Lattice iCE40 FPGAs. They also wrote a suite of command line tools for
> manipulating and creating bitstream files.

> The IceStorm flow includes two other tools: yosys and Arachne-pnr. Yosys is
> an open source verilog synthesis engine that maps verilog to ICE40
> primitives. Arachne-pnr is a place and router for the ICE40.

To install the icestorm tools, go to the [project icestorm
website](http://www.clifford.at/icestorm/) and follow the instructions under
**How to Install the Tools**.  Alternatively, you can try the
`scripts/install_icestorm.py` script which supports MacOS+homebrew and Ubuntu
Linux.

You will need to install:
* icestorm tools for generating bitstreams and programming the icestick
* arachne-pnr for placing and routing 
* yosys verilog synthesis tool

These programs should be installed into your shell environment's `$PATH`.

Note that if you are using a Mac, follow these
[instructions](http://www.clifford.at/icestorm/notes_osx.html).

One annoying problem on the Mac is the FTDI drivers.  There are three different
FTDI drivers for OSX:
1. Apple's driver
2. FTDI's driver
3. the open-source ftdi driver

In order to use the icestorm programmer, you need to uninstall the Apple and
FTDI drivers.  To see which driver is currently installed, run

```
kextstat | fgrep FTDI
```

And then remove the one that is installed.

```
$ sudo kextunload -b com.FTDI.driver.FTDIUSBSerialDriver
```

or

```
$ sudo kextunload -b com.apple.driver.AppleUSBFTDI
```

To reload the driver later, substitute `kextunload` with `kextload` in the
above command.

These drivers are installed on boot, so you may need to uninstall them again
every time you reboot.

### Python

If you don't have Python setup, we recommend using Miniconda

#### MacOS
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
$ bash Miniconda3-latest-MacOSX-x86_64.sh
```

#### Linux
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-MacOSX-x86_64.sh
```

Follow the prompts to install Miniconda and add Python to your PATH:

```
...
Please, press ENTER to continue
>>> [ENTER]
...
<scroll down>
...
Do you accept the license terms? [yes|no]
[no] >>> yes
...
   - Press ENTER to confirm the location
   - Press CRTL-C to abort the installation
   - Or specify a different location below

[/Users/yourusername/miniconda3] >>> [ENTER]
...
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /Users/yourusername/.bash_profile ? [yes|no]
[yes] >>> yes
```

### Magmathon

If all these tools are install and the repo cloned, you should be able to run
the programs in this hackathon.

First, clone the Magma Hackathon repo and run the script to install the
dependencies.

```
$ git clone git@github.com:phanrahan/magmathon.git
$ cd magmathon
$ python scripts/install.py
```

To validate that the installation was successful, we will compile a test Magma
program that blinks an LED on the IceStick.

```
$ cd tests
$ ls
Makefile blink.py
```

Build the program.
```
$ make
magma -b icestick blink.py
import mantle lattice ice40
import mantle lattice mantle40
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
Running the build script invokes the `magma` cli tool. We pass the `-b
icestick` argument to indicate to `magma` that we are compiling for the Lattice
icestick. 
`yosys`, the verilog synthesis tool, creates a file called `blink.blif`.
`arachne-pnr`, the place and router, takes as input `blink.blif` and produces
an ascii bit stream file `blink.txt`.  The `icepack` program converts the ascii
bit stream file to a binary bit stream file `blink.bin`.

Now plug in your icestick, and upload the the bitstream file.
```
$ make upload
iceprog blink.bin
```
The LED on the icestick should blink approximately 3 times per second.

Congratulations, everything is installed correctly and working!
