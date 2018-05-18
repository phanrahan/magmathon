import magma as m
from mantle import DFF
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

def FFs(n):
    def f(y):
        return DFF()
    return m.join(m.col(f, n))

def DefineRegister(n):
    reg = m.DefineCircuit('Register'+str(n),
               "I",   m.In(m.Bits(n)),
               "CLK", m.In(m.Clock),
               "O",   m.Out(m.Bits(n)))

    ffs = FFs(n)
    m.wire(ffs(reg.I), reg.O)
    m.wire(reg.CLK, ffs.CLK)

    m.EndCircuit()
    return reg

Register2 = DefineRegister(2)
register = Register2()

m.wire(register(I), O)

