import sys
import math
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
sawtooth = counter.O[8:8+4]

def int256(x):
    return int2seq(int(x), N)

sintab = [int256(128+127*math.sin(2 * math.pi * i / 16.)) for i in range(16)]
sintab = zip(*sintab) # transpose

print len(sintab)
print len(sintab[0])

def ROM(y):
    return ROM4(sintab[y])

rom = fork(col(ROM, N))

rom(sawtooth)

wire( rom, main.SIG )

compile(sys.argv[1], main)

