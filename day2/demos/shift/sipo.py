import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(1)
megawing.LED.on(8)

main = megawing.main()

def DefineSIPO(n):
    """
    Generate Serial-In, Parallel-Out shift register.

    I : Bit -> O : Array(n, Bit)
    """

    class _SIPO(Circuit):
        name = 'SIPO'+str(n)
        IO = ['input I', Bit, 'output O', Array(n,Bit)] + ClockInterface()

        @classmethod
        def definition(sipo):
            ffs = FFs(n)
            reg = braid(ffs, scanargs={"I":"O"})
            wire(sipo.I, reg.I)
            wire(reg.O, sipo.O)
            wireclock(sipo, reg)

    return _SIPO

SIPO8 = DefineSIPO(8)
sipo8 = SIPO8()

sipo8(main.SWITCH[0])
wire(sipo8, main.LED)

compile(sys.argv[1], main)
