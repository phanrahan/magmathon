import magma as m
from mantle import Register


@m.circuit.combinational
def uart_logic(
        writing : m.Bit,
        valid : m.Bit,
        dataStore : m.Bits(11),
        writeClock : m.Bits(14),
        writeBit : m.Bits(4),) -> (m.Bit,
                                   m.Bits(11),
                                   m.Bits(14),
                                   m.Bits(4),
                                   m.Bit,):

    if (writing == m.bit(0)) & (valid == m.bit(0)):
        writing_out = m.bit(1)
        # TODO(rsetaluri): fix this.
        dataStore_out = m.bits(0, 11)
        writeClock_out = m.bits(100, 14)
        writeBit_out = m.bits(0, 4)
        TXReg_out = dataStore[0]
    elif (writing == m.bit(1)) & \
         (writeClock == m.bits(0, 14)) & \
         (writeBit == m.bits(9, 4)):
        dataStore_out = dataStore
        writeClock_out = writeClock
        writeBit_out = writeBit
        TXReg_out = m.bit(1)
        writing_out = m.bit(0)
    elif (writing == m.bit(1)) & (writeClock == m.bits(0, 14)):
        writing_out = writing
        dataStore_out = dataStore
        TXReg_out = m.bit(0) #(dataStore >> m.uint(writeBit, 11))[0]
        writeBit_out = m.bits(m.uint(writeBit) + m.bits(1, 4))
        writeClock_out = m.bits(100, 14)
    elif writing == m.bit(1):
        writing_out = writing
        dataStore_out = dataStore
        writeBit_out = writeBit
        TXReg_out = m.bit(0) #(dataStore >> m.uint(writeBit, 11))[0]
        writeClock_out = m.bits(m.uint(writeClock) - m.bits(1, 14))
    else:
        writing_out = writing
        dataStore_out = dataStore
        writeClock_out = writeClock
        writeBit_out = writeBit
        TXReg_out = m.bit(1)

    return (writing_out,
            dataStore_out,
            writeClock_out,
            writeBit_out,
            TXReg_out,)


class UART(m.Circuit):
    IO = ["TX", m.Out(m.Bit),
          "data", m.In(m.Bits(8)),
          "valid", m.In(m.Bit),
          "ready", m.Out(m.Bit),]
    IO += m.ClockInterface()

    @classmethod
    def definition(io):
        TXReg = Register(1, init=1)
        dataStore = Register(11, init=1536)
        writing = Register(1, init=0)
        writeClock = Register(14, init=0)
        writeBit = Register(4, init=0)
        (writing_next,
         dataStore_next,
         writeClock_next,
         writeBit_next,
         TXReg_next,) = uart_logic(writing.O[0],
                                   io.valid,
                                   dataStore.O,
                                   writeClock.O,
                                   writeBit.O)
        m.wire(writing_next, writing.I[0])
        m.wire(dataStore_next, dataStore.I)
        m.wire(writeClock_next, writeClock.I)
        m.wire(writeBit_next, writeBit.I)
        m.wire(TXReg_next, TXReg.I[0])
        ready = writing.O[0] == m.bit(0)
        m.wire(ready, io.ready)
        m.wire(TXReg.O[0], io.TX)


if __name__ == "__main__":
    UART()
    m.compile("uart", UART, output="coreir")
