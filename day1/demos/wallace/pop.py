import magma as m
from loam.boards.icestick import IceStick
from wallace import wallace

N = 8
LOGN = 4

icestick = IceStick()
for i in range(N):
    icestick.J1[i].input().on()
for i in range(LOGN):
    icestick.J3[i].output().on()

main = icestick.main()

r = wallace([main.J1])
for i in range(len(r)):
    m.wire(r[i][0], main.J3[i])

