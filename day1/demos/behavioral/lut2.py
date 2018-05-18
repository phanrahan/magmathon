import magma as m
from mantle import LUT4, I0, I1, I2, I3
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D1.on()

main = icestick.main()

# I0, I1, I2 and I3 are 16-bit constants
#  bitwise operators with these constants are equivalent to composing functions
A = I0
B = I1
S0 = I2
S1 = I3
eqn = ((S0&S1)&(A^B))|((~S0&S1)&(A&B))|((S0&~S1)&(A|B))|((~S0&~S1)&(B))

logic = LUT4(eqn)

m.wire( logic(main.J1[0], main.J1[1], main.J1[2], main.J1[3]), main.D1 )
