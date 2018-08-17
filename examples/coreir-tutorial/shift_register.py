
# coding: utf-8

# In[1]:


import magma as m
m.set_mantle_target("coreir")
import mantle

def DefineShiftRegister(n, init=0, has_ce=False, has_reset=False):
    class _ShiftRegister(m.Circuit):
        name = 'ShiftRegister_{}_{}_{}_{}'.format(n, init, has_ce, has_reset)
        IO = ['I', m.In(m.Bit), 'O', m.Out(m.Bit)] +                m.ClockInterface(has_ce, has_reset)
        @classmethod
        def definition(siso):
            ffs = mantle.FFs(n, init=init, has_ce=has_ce, has_reset=has_reset)
            reg = m.braid(ffs, foldargs={"I":"O"})
            reg(siso.I)
            m.wire(reg.O, siso.O)
            m.wireclock(siso, reg)
    return _ShiftRegister


# In[2]:


m.compile("build/DefineShiftRegister.json", DefineShiftRegister(2, has_ce=True), output="coreir")
get_ipython().magic('cat build/DefineShiftRegister.json')


# In[3]:


from magma.simulator.coreir_simulator import CoreIRSimulator
from bit_vector import BitVector

N = 3
ShiftRegisterNCE = DefineShiftRegister(N, has_ce=True)
simulator = CoreIRSimulator(ShiftRegisterNCE, clock=ShiftRegisterNCE.CLK)
outputs = []
for j in range(2):
    simulator.advance()
for I, enable in [(1, 1), (0, 1), (1, 1), (0, 1), (1, 0), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1)]:
    simulator.set_value(ShiftRegisterNCE.I, bool(I))
    simulator.set_value(ShiftRegisterNCE.CE, bool(enable))
    for j in range(2):
        simulator.advance()
        O = simulator.get_value(ShiftRegisterNCE.O)
        CLK = simulator.get_value(ShiftRegisterNCE.CLK)
        outputs.append([O, I, enable, CLK])


# In[4]:


from magma.waveform import waveform

waveform(outputs, ["O", "I", "CE", "CLK"])

