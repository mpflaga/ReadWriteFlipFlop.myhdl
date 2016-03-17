from myhdl import toVerilog, toVHDL, always, Signal, intbv

def dff(q, d, wr, rst):

    @always(wr.posedge, rst.negedge)
    def logic():
        if rst == 0:
            q.next = 0
        else:
            q.next = d

    return logic
    
def convert():
    q = Signal(intbv(0)[1:0])
    d = Signal(intbv(0)[1:0])
    wr, rst = [Signal(bool(0)) for i in range(2)]

    toVerilog(dff, q, d, wr, rst)
    toVHDL(dff, q, d, wr, rst)

if __name__ == '__main__':
    convert()

