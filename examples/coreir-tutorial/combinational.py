
# coding: utf-8

# In[1]:


import magma as m
m.set_mantle_target("coreir")
import mantle

class Combinational(m.Circuit):
    name = "Combinational"
    IO = ["x", m.In(m.UInt(16)), "y", m.In(m.UInt(16)), "z", m.Out(m.UInt(16))]
    
    @classmethod
    def definition(io):
        m.wire(io.x + io.y, io.z)


# In[2]:


from magma.simulator.coreir_simulator import CoreIRSimulator
from bit_vector import BitVector

simulator = CoreIRSimulator(Combinational, clock=None)
simulator.set_value(Combinational.x, BitVector(76, num_bits=16))
simulator.set_value(Combinational.y, BitVector(43, num_bits=16))
simulator.evaluate()
assert BitVector(simulator.get_value(Combinational.z)) == BitVector(76 + 43, num_bits=16)
print("Success!")


# In[3]:


m.compile("build/Combinational", Combinational, output="coreir")
get_ipython().magic('cat build/Combinational.json')

