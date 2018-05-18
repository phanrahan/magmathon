import magma as m
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].input().on()
icestick.J1[1].input().on()
icestick.J3[0].output().on()
icestick.J3[1].output().on()

main = icestick.main()

HalfAdder = m.DefineCircuit('Add', 
   'A', m.In(m.Bit), 
   'B', m.In(m.Bit),
   'S', m.Out(m.Bit),
   'C', m.Out(m.Bit))
HalfAdder.verilog  = '''\
    assign S = A ^ B;
    assign C = A & B;\
'''
m.EndCircuit()

add = HalfAdder()
add(main.J1[0], main.J1[1])
m.wire(add.S, main.J3[0])
m.wire(add.C, main.J3[1])


