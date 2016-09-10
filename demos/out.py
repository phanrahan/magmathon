import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()

wire( 1, main.D1 )
wire( 1, main.D2 )

compile(sys.argv[1], main)

