import magma as m
from mantle import FFs
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].input().on()
icestick.J1[1].input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
I = main.J1
O = m.array([main.D1, main.D2])

def DefineRegister(n):
    """
    Generate an n-bit register
    
    I : Bits(n) -> O : Bits(n)
    """ 
    T = m.Bits(n)
    class _Register(m.Circuit):
        name = 'Register'+str(n)
        IO  = ['I', m.In(T), 'O', m.Out(T), "CLK", m.In(m.Clock)]

        @classmethod
        def definition(reg):
            ffs = m.join(FFs(n))
            m.wire(reg.I, ffs.I) 
            m.wire(ffs.O, reg.O)
            m.wire(reg.CLK, ffs.CLK)
    return _Register

Register2 = DefineRegister(2)
register2 = Register2()

m.wire(register2(I), O)

