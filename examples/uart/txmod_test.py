import fault
import magma
from txmod import TXMOD
import random


def get_random(port):
    if isinstance(port, magma.BitType):
        return random.choice((0, 1))
    N = type(port).N
    return random.randint(0, 2 ** N - 1)


if __name__ == "__main__":
    random.seed(0)

    #TXMOD_v = magma.DefineFromVerilogFile("examples/uart/txmod.v")[0]
    circ = TXMOD
    tester = fault.Tester(circ, circ.CLK)
    magma.compile("build/TXMOD", circ, output="coreir-verilog")

    inputs = {}
    outputs = {}
    for name, port in circ.interface.ports.items():
        if port is circ.CLK:
            continue
        if port.isoutput():
            inputs[name] = port
        elif port.isinput():
            outputs[name] = port

    tester.poke(circ.CLK, 0)
    for i in range(2):
        #tester.print_string("=========================================")
        tester.print_string("========== inputs ====================")
        for name, port in inputs.items():
            tester.poke(port, get_random(port))
            tester.print_format(f"{name}: %p\\n", port)
        tester.print_format(f"CLK: %p\\n", circ.CLK)
        tester.step()
        tester.print_format(f"CLK: %p\\n", circ.CLK)
        tester.print_string("========== outputs ====================")
        for name, port in outputs.items():
            tester.print_format(f"{name}: %p\\n", port)

    tester.compile_and_run(target="verilator", flags=["-Wno-fatal"], skip_compile=True)
