
# coding: utf-8

# In[1]:


import magma as m
m.set_mantle_target("coreir")
import mantle


# This notebook demonstrates using native Python functions to construct circuits.

# In[2]:


def clb(a, b, c, d):
    return (a & b) | (~c & d)

T = m.UInt(16)
class Combinational(m.Circuit):
    name = "Combinational"
    IO = ["a", m.In(T), "b", m.In(T), "c", m.Out(T)]
    @classmethod
    def definition(io):
        m.wire(clb(io.a, io.b, io.a, io.b), io.c)


# In[3]:


from magma.simulator import PythonSimulator
from magma.bit_vector import BitVector

simulator = PythonSimulator(Combinational)
a = BitVector(148, num_bits=16)
b = BitVector(41, num_bits=16)
simulator.set_value(Combinational.a, a)
simulator.set_value(Combinational.b, b)
simulator.evaluate()
assert BitVector(simulator.get_value(Combinational.c)) == clb(a, b, a, b)
print("Success!")


# In[4]:


m.compile("build/Combinational", Combinational, output="coreir")
get_ipython().magic('cat build/Combinational.json')

