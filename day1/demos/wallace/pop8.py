import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(8)
megawing.LED.on(4)

main = megawing.main()
I = main.SWITCH
O = main.LED

def CSA():
    return fork([LUT3(I0^I1^I2), LUT3((I0&I1)|(I1&I2)|(I2&I0))])

# Dadda dot notation
# o o
# o o 
# o o 
csa0_0_21 = CSA()(I[0], I[1], I[2])
csa0_1_21 = CSA()(I[3], I[4], I[5])
csa0_2_21 = CSA()(I[6], I[7], 0)

#   o o
# o o 
csa1_0_21 = CSA()(csa0_0_21.O[0], csa0_1_21.O[0], csa0_2_21.O[0])
csa1_0_42 = CSA()(csa0_0_21.O[1], csa0_1_21.O[1], csa0_2_21.O[1])

#     o
# o o o
csa2_0_42 = CSA()(csa1_0_21.O[1], csa1_0_42.O[0], 0)

# o o o o 
csa2_0_84 = CSA()(csa1_0_42.O[1], csa2_0_42.O[0], 0)

wire(csa1_0_21.O[0], O[0])
wire(csa2_0_42.O[0], O[1])
wire(csa2_0_84.O[0], O[2])
wire(csa2_0_84.O[1], O[3])

compile(sys.argv[1], main)
