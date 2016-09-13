import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on() # need to turn the clock on
icestick.PMOD[0].rename('S1').input().on()
icestick.D1.on()

main = icestick.main()
I = main.S1
O = main.D1

# create ff holding state first
ff = FF()

# lut computes the next state ...
#  function of the previous state and the input
lut = LUT2( I0^I1 )
lut(I, ff)

# lut computes the next state
ff(lut)

wire( ff, O )

compile(sys.argv[1], main)
