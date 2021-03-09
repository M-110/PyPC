from .nand import nand


def mux(selector: bool, a: bool, b: bool) -> bool:
    """Multiplexer: returns a if selector is True, otherwise returns b."""
    not_selector = nand(selector, selector)
    nand_s_a = nand(selector, a)
    nand_not_s_b = nand(not_selector, b)
    return nand(nand_s_a, nand_not_s_b)


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
