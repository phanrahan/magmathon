import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(1)
megawing.LED.on(1)

main = megawing.main()

def DefineSISO(n):
    """
    Generate Serial-In, Serial-Out shift register.

    I : Bit -> O : Bit
    """

    class _SISO(Circuit):
        name = 'SISO'+str(n)
        IO = ['input I', Bit, 'output O', Bit] + ClockInterface()

        @classmethod
        def definition(siso):
            ffs = FFs(n)
            reg = braid(ffs, foldargs={"I":"O"})
            reg(siso.I)
            wire(reg.O, siso.O)
            wireclock(siso, reg)

    return _SISO

SISO8 = DefineSISO(8)
siso8 = SISO8()

siso8(main.SWITCH[0])
wire(siso8, main.LED[0])

compile(sys.argv[1], main)
