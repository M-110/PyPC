from pypc.a_primitives.nand import nand

# nand gates used: 4
from pypc.pypc_typing import Bool2, Bool4, Bool3, Bool8


def mux(selector: bool, a: bool, b: bool) -> bool:
    """Multiplexer: returns a if selector is True, otherwise returns b."""
    not_selector = nand(selector, selector)
    nand_s_a = nand(selector, a)
    nand_not_s_b = nand(not_selector, b)
    return nand(nand_s_a, nand_not_s_b)


# nand gates used: 5
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


# nand gates used: 15
def demux_4way(in_: bool, selectors: Bool2) -> Bool4:
    x, y = demux(selectors[1], in_)
    a, b = demux(selectors[0], x)
    c, d = demux(selectors[0], y)
    return a, b, c, d


# nand gates used: 35
def demux_8way(in_: bool, selectors: Bool3) -> Bool8:
    x, y = demux(selectors[2], in_)
    a, b, c, d = demux_4way(x, selectors[0:2])
    e, f, g, h = demux_4way(y, selectors[0:2])
    return a, b, c, d, e, f, g, h
