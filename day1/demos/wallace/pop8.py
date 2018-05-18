import magma as m
from magma.bitutils import clog2
from mantle import LUT3, I0, I1, I2
from loam.boards.icestick import IceStick

N = 128
LOGN = min( clog2(N) + 1, 8 )

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
for i in range(LOGN):
    icestick.J3[i].output().on()

main = icestick.main()
I = main.J1
O = main.J3

def CSA():
    return m.fork([LUT3(I0^I1^I2), LUT3((I0&I1)|(I1&I2)|(I2&I0))])

def csa(a, b, c):
    return CSA()(a, b, c)

# Dadda dot notation
# o o
# o o 
# o o 
csa0_0_21 = csa(I[0], I[1], I[2])
csa0_1_21 = csa(I[3], I[4], I[5])
csa0_2_21 = csa(I[6], I[7], 0)

#   o o
# o o 
csa1_0_21 = csa(csa0_0_21[0], csa0_1_21[0], csa0_2_21[0])
csa1_0_42 = csa(csa0_0_21[1], csa0_1_21[1], csa0_2_21[1])

#     o
# o o o
csa2_0_42 = csa(csa1_0_21[1], csa1_0_42[0], 0)

# o o o o 
csa2_0_84 = csa(csa1_0_42[1], csa2_0_42[0], 0)

m.wire(csa1_0_21[0], O[0])
m.wire(csa2_0_42[0], O[1])
m.wire(csa2_0_84[0], O[2])
m.wire(csa2_0_84[1], O[3])

