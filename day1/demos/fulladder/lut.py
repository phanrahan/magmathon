import magma as m
from mantle import LUT3, I0, I1, I2
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].input().on()
icestick.J1[1].input().on()
icestick.J1[2].input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()

def FullAdder():
    return m.fork([LUT3(I0^I1^I2), LUT3((I0&I1)|(I1&I2)|(I2&I0))])

fulladder = FullAdder()

S, C = fulladder(main.J1[0], main.J1[1], main.J1[2])

m.wire( S, main.D1 )
m.wire( C, main.D2 )

