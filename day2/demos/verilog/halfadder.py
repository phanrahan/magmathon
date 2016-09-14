import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(2)
megawing.LED.on(1)

main = megawing.main()

HalfAdder = DefineCircuit('Add', 
   'input A', Bit, 
   'input B', Bit,
   'output S', Bit,
   'output C', Bit)
HalfAdder.verilog  = '''\
    assign S = A ^ B;
    assign C = A & B;\
'''
EndCircuit()

add = HalfAdder()
add(main.SWITCH[0], main.SWITCH[1])
wire(add.C, main.LED[0])

compile(sys.argv[1], main)

