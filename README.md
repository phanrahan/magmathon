# Gettting Started with Magma and Mantle on the Icestick

We will be using Magma with an Lattice Icestick.
The Icestick is a small FPGA with an open-source tool chain.

![icestick](images/icestick.jpg)

### Icestorm tools

To install the icestorm tools, go to the [project
icestorm](http://www.clifford.at/icestorm/) web site and follow the
instructions under "How to Install the Tools".

You will need to install:
* icestorm tools for generating bitstreams and programming the icestick
* arachne-pnr for placing and routing 
* yosys verilog synthesis tool

These programs should be installed into your shell environment's `$PATH`.

Note that if you are using a Mac, follow these
[instruction](http://www.clifford.at/icestorm/notes_osx.html).

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
% sudo kextunload -b com.FTDI.driver.FTDIUSBSerialDriver
% sudo kextunload -b com.apple.driver.AppleUSBFTDI
```

These drivers are installed on boot, and may need to be installed if you
reboot.

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
% git clone git@github.com:phanrahan/magmathon.git
% python scripts/install.py
```

Then build the examples.

```
% cd magmathon/tests
% . doit
python counter.py build/counter
importing lattice ice40
importing lattice mantle40
setup clock
setup clock
compiling Adc22_1
compiling Register22
compiling Counter22
compiling main
cmp build/counter.ucf gold/counter.ucf
cmp build/counter.v gold/counter.v
python inout.py build/inout
importing lattice ice40
importing lattice mantle40
compiling main
cmp build/inout.ucf gold/inout.ucf
cmp build/inout.v gold/inout.v
python out.py build/out
importing lattice ice40
importing lattice mantle40
compiling main
cmp build/out.ucf gold/out.ucf
cmp build/out.v gold/out.v

```

The script, `doit` builds two programs, `counter.py` and `out.py`.
That script is pretty simple,

```
% cat doit
export MANTLE=lattice
export MANTLE_TARGET=ice40
./bake clean
./bake
%
```
To use the icestick board with Magma,
you need to set the MANTLE and MANTLE_TARGET environment variables.
```
% export MANTLE=lattice
% export MANTLE_TARGET=ice40
```
These variables causes magma to use the lattice ice40 version
of the mantle library.

The build script is called `bake`.
`bake` is like `make`, but it uses `fabricate`.

The output of the build script is placed in the `build` directory.
```
% cd build
% ls
Makefile    counter.v   inout.v     out.v
counter.ucf inout.ucf   out.ucf
```
To build a bitstream for the icestick, run make.
```
% make
yosys -q -p 'synth_ice40 -top main -blif counter.blif' counter.v
arachne-pnr -q -d 1k -o counter.txt -p counter.ucf counter.blif 
icepack counter.txt counter.bin
```
`yosys` is the verilog synthesizer;
it creares a file called "counter.blif".
`arachne-pnr` is the place and router;
it takes as input "counter.blif", 
and produces an ascii bit stream file "counter.txt".
The program `icepack` converts the ascii bit stream file
to a binary bit stream file "counter.bin"..

Now plug in your icestick,
and upload the the bitstream file.
```
% make upload
iceprog counter.bin
```
The LED on the icestick should blink approximately 3 times per second.

Congratulations, everything is installed correctly and working!




