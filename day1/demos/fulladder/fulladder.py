import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.PMOD[0].rename('S1').input().on()
icestick.PMOD[1].rename('S2').input().on()
icestick.PMOD[2].rename('S3').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
I = Array3(main.S1, main.S2, main.S3)
O = Array2(main.D1, main.D2)

def FullAdder():
    return fork([ROM3(I0^I1^I2), ROM3((I0&I1)|(I1&I2)|(I2&I0))])

fa = FullAdder()
print "FullAdder ::", fa.interface

wire( fa(I), O )

compile(sys.argv[1], main)
