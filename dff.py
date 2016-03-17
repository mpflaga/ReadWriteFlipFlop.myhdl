from myhdl import toVerilog, toVHDL, always, Signal, intbv

def dff(q, d, wr, rst):
    """ A scalable Tri-State Buffer

    I/O pins:
    --------
    q   : output; buffer the data comes in on and leaves out. 
    d   : input; signal to be latched.
    wr  : input; signal indicating when to latch data.
    rst : input; signal indicating clear of latch data.

    """

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

