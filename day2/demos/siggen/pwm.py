import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

N = 8

def PWM(n):
    return ULE(n)

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD[0].rename('SIG').output().on()

main = icestick.main()

counter = Counter(32)
sawtooth = counter.O[8:8+N]

pwm = PWM(N)
pwm( sawtooth, array(0,0,0,0,0,0,1,0) )
wire( pwm, main.SIG )

compile(sys.argv[1], main)

