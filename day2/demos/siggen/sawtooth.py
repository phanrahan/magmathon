import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

N = 8

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD[0].rename('SIG[0]').output().on()
icestick.PMOD[1].rename('SIG[1]').output().on()
icestick.PMOD[2].rename('SIG[2]').output().on()
icestick.PMOD[3].rename('SIG[3]').output().on()
icestick.PMOD[6].rename('SIG[4]').output().on()
icestick.PMOD[7].rename('SIG[5]').output().on()
icestick.PMOD[8].rename('SIG[6]').output().on()
icestick.PMOD[9].rename('SIG[7]').output().on()

main = icestick.main()

counter = Counter(32)
sawtooth = counter.O[8:8+N]

wire( sawtooth, main.SIG )

compile(sys.argv[1], main)

