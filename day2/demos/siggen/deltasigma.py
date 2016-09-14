import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

DELTA = 0x8000

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD[0].rename('SIG').output().on()

main = icestick.main()

add = AddC(16)
reg = Register(16)

reg( add(reg, Array16(*int2seq(DELTA,16))) )

wire( add.COUT, main.SIG )

compile(sys.argv[1], main)

