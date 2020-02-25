import logging
logging.basicConfig(level=logging.INFO)
import magma as m
import mantle
import fault


def test_install():
    class Main(m.Circuit):
        io = m.IO(I=m.In(m.Bit), O=m.Out(m.Bit), CLK=m.In(m.Clock))
        reg = mantle.Register(None)
        io.O @= reg(io.I)


    tester = fault.Tester(Main, Main.CLK)
    tester.circuit.I = 0
    tester.circuit.CLK = 0
    tester.step(2)
    tester.circuit.I = 1
    tester.circuit.O.expect(0)
    tester.step(2)
    tester.circuit.I = 0
    tester.circuit.O.expect(1)
    tester.step(2)
    tester.circuit.O.expect(0)
    tester.compile_and_run("verilator")


if __name__ == "__main__":
    test_install()
