
# coding: utf-8

# In[1]:


import magma as m
m.set_mantle_target("coreir")
import mantle

def DefineAdder(N):
    T = m.UInt(N)
    class Adder(m.Circuit):
        name = "Adder{}".format(N)
        IO = ["I0", m.In(T), "I1", m.In(T), "CIN", m.In(m.Bit),
              "O", m.Out(T), "COUT", m.Out(m.Bit)]
        @classmethod
        def definition(io):
            adders = [mantle.FullAdder() for _ in range(N)]
            adders = m.fold(adders, foldargs={"CIN":"COUT"})
            COUT, O = adders(I0=io.I0, I1=io.I1, CIN=io.CIN)
            m.wire(O, io.O)
            m.wire(COUT, io.COUT)
    return Adder

Adder4 = DefineAdder(4)


# In[2]:


print(repr(Adder4))


# In[3]:


m.compile("build/Adder4", Adder4, output="coreir")
get_ipython().magic('cat build/Adder4.json')


# In[4]:


from fault.test_vectors import generate_simulator_test_vectors
import fault

tests = generate_simulator_test_vectors(Adder4, flatten=False)
print(" a  b  ci o  co")
for test in tests:
    for t in test:
        print("{:2d}".format(t.as_uint()), end=' ')
    print()

