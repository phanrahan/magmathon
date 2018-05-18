import magma as m
from mantle import LUT2, I0, I1, And
from loam.boards.icestick import IceStick

def And2(y):
    return LUT2(I0&I1)

def And(n):
    return m.join(m.col(And2, n))


icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J1[i].input().on()
for i in range(4):
    icestick.J3[i].output().on()

main = icestick.main()

a = And(4)

m.wire( a(main.J1[0:4], main.J1[4:8]), main.J3 )

