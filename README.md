Welcome to the homepage for the magmathon! See [the magma
repository](https://github.com/phanrahan/magma) for more information on
the embedded hardware design language.

If you are participating in the hackathon,
you should try to install the required software in advance.
Don't worry if you run into problems,
we will debug them first thing.
You should also identify a small project that you would like to
try to implement.  See [this page](./projects/README.md) for examples of previous projects.

The next hackathon will be held on Wednesday, March 4th at Stanford.
Please contact [@leonardt](https://github.com/leonardt) if you're interested in
attending.


# Schedule
```
 9:00am -  9:30am -- Setup and Installation
 9:30am -  9:45am -- Magma Ecosystem Overview 
 9:45am - 11:00am -- Magma Tutorial
11:00am - 12:00pm -- Freeform Hacking
12:00pm -  1:30pm -- Lunch
 1:30pm -  2:30pm -- (optional) Advanced Magma
 1:30pm -  4:00pm -- Freeform Hacking
 4:00pm -  4:30pm -- Show and Tell, Feedback, Debrief
```

# Session Overviews

## Setup and Installation
Magma requires Python 3.7.
If you don't have Python setup, we recommend using Miniconda

#### MacOS
```
$ curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
$ bash Miniconda3-latest-MacOSX-x86_64.sh
```

#### Linux
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```

#### Windows
We recommend using a Linux virtual machine


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

### Install third-party libraries
You'll also need some third party libraries for simulation and the
[hwtypes](https://github.com/leonardt/hwtypes) python package:
* Debian
  ```
  $ apt install verilator libgmp-dev libmpfr-dev libmpc-dev
  ```

* MacOS
  Requires [homebrew](https://brew.sh)
  ```
  $ brew install verilator gmp mpfr libmpc
  ```

### Install python packages
Install the magma ecosystem using the following pip command
```shell
pip install magma-lang mantle fault
```

If you'd like to run the jupyter notebooks, install it with conda
```
conda install -c conda-forge notebook
```
or pip
```
pip install notebook
```

### Setup Magmathon Repository
Clone the magmathon repository
```
git clone https://github.com/phanrahan/magmathon.git
```

To validate the installation was succesful, we will run a simple magma program
```
$ cd magmathon/tests
$ python test_install.py
...
INFO:root:Running tester...
INFO:root:Success!
```

## Magma Ecosystem Overview
This session will present a high-level overview of the Magma ecosystem: a set
of Python packages for hardware design.  This will cover how a Python-embedded
hardware design language serves as the basis for a suite of productivity tools
including verification infrastructure and high-level DSLs.

## Magma Tutorial
The tutorial covers the basics of the magma hardware design language,
introducing users to the circuit abstraction, wiring, types, and operators.  

## Freeform hacking
The afternoon will be devoted free form hacking where attendees are free to
hack wherever they want. The goal of this hackathon is to support self
organizing projects, so we’ll mainly be providing space, materials, and support
for attendees.  Please submit a PR that adds a link to your project repository
to [projects/README.md](/projects/README.md).


## Advanced Magma (optional)
This will be an informal session on the advanced magma features for building
complex generators including introspection, metaprogramming, and testing.  The
exact topics covered will depend on interest, so we will poll attendees to see
what will be most relevant for their projects.  At this point, attendees are
also welcome to get started on their hackathon projects.  
