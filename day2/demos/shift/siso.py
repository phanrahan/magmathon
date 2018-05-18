import magma as m
from mantle import FFs
from loam.boards.icestick import IceStick

N = 8

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('J1').input().on()
icestick.J3[0].rename('J3').output().on()

def DefineSISO(n):
    """
    Generate Serial-In, Serial-Out shift register.

    I : Bit -> O : Bit
    """

    class _SISO(m.Circuit):
        name = 'SISO'+str(n)
        IO = ['I', m.In(m.Bit), 'O', m.Out(m.Bit)] + m.ClockInterface()

        @classmethod
        def definition(siso):
            ffs = FFs(n)
            reg = m.braid(ffs, foldargs={"I":"O"})
            reg(siso.I)
            m.wire(reg.O, siso.O)
            m.wireclock(siso, reg)

    return _SISO

main = icestick.main()

SISO8 = DefineSISO(8)
siso8 = SISO8()

m.wire( siso8(main.J1), main.J3 )

