import magma as m
from mantle import LUT4
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D1.on()

main = icestick.main()

logic = LUT4([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])

m.wire( logic(main.J1[0], main.J1[1], main.J1[2], main.J1[3]), main.D1 )
