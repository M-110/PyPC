from pypc.a_primitives.nand import nand
from pypc.b_basic_logic.selectors import mux
from typing import Tuple

Bool16 = Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]


# nand gates used: 64
def mux_16(selector: bool, a: Bool16, b: Bool16) -> Bool16:
    """Multiplexer 16: returns a if selector is True, otherwise returns b."""
    return (mux(selector, a[0], b[0]),
            mux(selector, a[1], b[1]),
            mux(selector, a[2], b[2]),
            mux(selector, a[3], b[3]),
            mux(selector, a[4], b[4]),
            mux(selector, a[5], b[5]),
            mux(selector, a[6], b[6]),
            mux(selector, a[7], b[7]),
            mux(selector, a[8], b[8]),
            mux(selector, a[9], b[9]),
            mux(selector, a[10], b[10]),
            mux(selector, a[11], b[11]),
            mux(selector, a[12], b[12]),
            mux(selector, a[13], b[13]),
            mux(selector, a[14], b[14]),
            mux(selector, a[15], b[15]))


def demux(selector: bool, in_: bool) -> (bool, bool):
    """Demultiplexer: Returns pairs of bools (a, b) based on selector.

    If selector is True, a will equal the input.
    If selector is False, b will equal the input.

    The non-selected output will always be false."""
    not_selector = nand(selector, selector)
    nand_not_s_in = nand(not_selector, in_)
    nand_s_in = nand(selector, in_)
    a = nand(nand_s_in, nand_s_in)
    b = nand(nand_not_s_in, nand_not_s_in)
    return a, b
