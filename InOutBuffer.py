from myhdl import always_comb, TristateSignal, Signal, toVerilog, toVHDL

def InOutBuffer(t, i, o, dir):
    """ A scalable Tri-State Buffer

    I/O pins:
    --------
    t   : tristated buffer the data comes in on and leaves out. 
    i   : output; signal from the tristate buffer.
    o   : input; signal to go out on the tristate buffer.
    dir : input; signal driving direction of tristate buffer.

    """
    
    b_d = t.driver()

    @always_comb
    def hdl():
        i.next = t
        b_d.next = o if dir else None

    return hdl


def convert():
     t = TristateSignal(True)
     i = Signal(False)
     o = Signal(False)
     dir = Signal(False)

     toVerilog(InOutBuffer, t, i, o, dir)
     toVHDL(InOutBuffer, t, i, o, dir)

if __name__ == '__main__':
     convert()

