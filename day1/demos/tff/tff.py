import magma as m
from mantle import FF, xor
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on() # need to turn the clock on
icestick.J1[0].rename('J1').input().on()
icestick.D1.on()

main = icestick.main()

# first, create flip-flop 
ff = FF()

m.wire( ff( xor(main.J1, ff.O) ), main.D1 )


