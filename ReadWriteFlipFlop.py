from myhdl import Signal, TristateSignal, intbv, toVerilog, toVHDL, always

from InOutBuffer import InOutBuffer
from dff import dff

def ReadWriteFlipFlop(t, dir, wr, rst):
    """ A scalable Tri-State Buffer

    I/O pins:
    --------
    t   : tristated buffer the data comes in on and leaves out. 
    dir : input; signal driving direction of tristate buffer.
    wr  : input; signal indicating when to latch data.
    rst : input; signal indicating clear of latch data.

    """

    i = Signal(intbv(0)[len(t):])
    q = Signal(intbv(0)[len(t):])
    data = InOutBuffer(t, i, q, dir)
    dff_inst = dff(q, i, wr, rst)

    return data, dff_inst

def convert():

    pins = 10
    t = TristateSignal(intbv(1)[pins:])
    dir = Signal(bool(0))
    wr, rst = [Signal(bool(0)) for i in range(2)]

    toVerilog(ReadWriteFlipFlop, t, dir, wr, rst)
    toVHDL(ReadWriteFlipFlop, t, dir, wr, rst)

convert()