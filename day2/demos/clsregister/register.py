import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD[0].rename('S1').input().on()
icestick.PMOD[1].rename('S2').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
I = Array2(main.S1, main.S2)
O = Array2(main.D1, main.D2)

def DefineRegister(n):
    """
    Generate an n-bit register
    
    I : Array(n, Bit) -> O : Array(n, Bit)
    """ 
    
    T = Array(n, Bit)
    class _Register(Circuit):
        name = 'Register'+str(n)
        IO  = ['input I', T, 'output O', T, "input CLK", Bit]

        @classmethod
        def definition(reg):
            ffs = join(FFs(n))
            wire(reg.I, ffs.I) 
            wire(ffs.O, reg.O)
            wire(reg.CLK, ffs.CLK)
    return _Register

Register2 = DefineRegister(2)
register2 = Register2()

wire(register2(I), O)

compile(sys.argv[1], main)
