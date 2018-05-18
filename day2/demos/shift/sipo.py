import magma as m
from mantle import FFs
from loam.boards.icestick import IceStick

N = 8

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('J1').input().on()
for i in range(N):
    icestick.J3[i].output().on()

def DefineSIPO(n):
    """
    Generate Serial-In, Parallel-Out shift register.

    I : Bit -> O : Array(n, Bit)
    """

    class _SIPO(m.Circuit):
        name = 'SIPO'+str(n)
        IO = ['I', m.In(m.Bit), 'O', m.Out(m.Bits(n))] + m.ClockInterface()

        @classmethod
        def definition(sipo):
            ffs = FFs(n)
            reg = m.braid(ffs, scanargs={"I":"O"})
            m.wire(sipo.I, reg.I)
            m.wire(reg.O, sipo.O)
            m.wireclock(sipo, reg)

    return _SIPO

main = icestick.main()

SIPO8 = DefineSIPO(8)
sipo8 = SIPO8()

m.wire( sipo8(main.J1), main.J3 )

