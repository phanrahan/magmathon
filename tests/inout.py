import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.PMOD[0].rename('I1').input().on()
icestick.PMOD[1].rename('I2').input().on()
icestick.PMOD[2].rename('I3').input().on()
icestick.PMOD[3].rename('I4').input().on()
icestick.D1.on()
icestick.D2.on()
icestick.D3.on()
icestick.D4.on()

main = icestick.main()

wire( main.I1, main.D1 )
wire( main.I2, main.D2 )
wire( main.I3, main.D3 )
wire( main.I4, main.D4 )

compile(sys.argv[1], main)
