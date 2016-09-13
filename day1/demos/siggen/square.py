import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD[9].rename('SIG').output().on()

main = icestick.main()

counter = Counter(32)
square = counter.O[9]

wire( square, main.SIG )

compile(sys.argv[1], main)

