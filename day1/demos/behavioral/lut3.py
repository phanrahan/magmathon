import magma as m
from mantle import LUT4
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D1.on()

main = icestick.main()

def f(I0, I1, I2, I3):
    if I3:
        if I2: return I0^I1
        else:  return I0&I1
    else:
        if I2: return I0|I1
        else:  return I1

logic = LUT4(f)

m.wire( logic(main.J1[0], main.J1[1], main.J1[2], main.J1[3]), main.D1 )
