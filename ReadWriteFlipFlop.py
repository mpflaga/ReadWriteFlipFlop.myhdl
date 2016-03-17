from myhdl import Signal, TristateSignal, intbv, toVerilog, toVHDL, always

from InOutBuffer import InOutBuffer
from dff import dff

pins = 10

t = TristateSignal(intbv(1)[pins:])
dir = Signal(bool(0))
wr, rst = [Signal(bool(0)) for i in range(2)]

def ReadWriteFlipFlop(t, dir, wr, rst):
    i = Signal(intbv(0)[pins:])
    q = Signal(intbv(0)[pins:])
    data = InOutBuffer(t, i, q, dir)
    dff_inst = dff(q, i, wr, rst)

    return data, dff_inst

def convert():

    toVerilog(ReadWriteFlipFlop, t, dir, wr, rst)
    toVHDL(ReadWriteFlipFlop, t, dir, wr, rst)

convert()