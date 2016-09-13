import sys
from magma import *
from mantle import *
from wallace import wallace
from shields.megawing import MegaWing

N = 8
M = 4

megawing = MegaWing()
megawing.Switch.on(N)
megawing.LED.on(M)

main = megawing.main()
I = main.SWITCH
O = main.LED

r = wallace([main.SWITCH])
for i in range(len(r)):
    wire(r[i][0], main.LED[i])

compile(sys.argv[1], main)
