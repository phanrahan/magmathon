
# coding: utf-8

# In[1]:


import magma as m
m.set_mantle_target("coreir")
import mantle

class FullAdder(m.Circuit):
    name = "FullAdderExample"  # Note: We use a unique name here 
                               # to avoid conflict with the Circuit 
                               # called FullAdder that is a part of 
                               # the mantle standard library
    IO = ["a", m.In(m.Bit), "b", m.In(m.Bit), "cin", m.In(m.Bit),
          "out", m.Out(m.Bit), "cout", m.Out(m.Bit)]
    @classmethod
    def definition(io):
        # Generate the sum
        _sum = io.a ^ io.b ^ io.cin
        m.wire(_sum, io.out)
        # Generate the carry
        carry = (io.a & io.b) | (io.b & io.cin) | (io.a & io.cin)
        m.wire(carry, io.cout)


# In[2]:


m.compile("build/FullAdder", FullAdder, output="coreir")
get_ipython().magic('cat build/FullAdder.json')


# In[3]:


m.compile("build/FullAdder", FullAdder, output="coreir-verilog")
get_ipython().magic('cat build/FullAdder.v')


# In[4]:


from fault.test_vectors import generate_simulator_test_vectors
from bit_vector import BitVector

test_vectors_raw = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

test_vectors = [
    [BitVector(x) for x in test_vector]
    for test_vector in test_vectors_raw
]

tests = generate_simulator_test_vectors(FullAdder, flatten=False)
print( "Success" if tests == test_vectors else "Failure" )


# In[5]:


from magma.waveform import waveform

waveform(test_vectors_raw, ["a", "b", "cin", "sum", "cout"])

