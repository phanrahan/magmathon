import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(4)

main = megawing.main()

def And2(y):
    return LUT2(I0&I1)

def And(n):
    return join(col(And2, n))

a = And(4)

a(main.SWITCH[0:4], main.SWITCH[4:8])
wire(a.O, main.LED)

compile(sys.argv[1], main)
