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

def FFs(n):
    def f(y):
        return DFF()
    return join(col(f, n))

def DefineRegister(n):
    reg = DefineCircuit('Register'+str(n),
               "input I", Array(n,Bit),
               "input CLK", Bit,
               "output O", Array(n,Bit))

    ffs = FFs(n)
    wire(ffs(reg.I), reg.O)
    wire(reg.CLK, ffs.CLK)

    EndCircuit()
    return reg

Register2 = DefineRegister(2)
register = Register2()

wire(register(I), O)

compile(sys.argv[1], main)
