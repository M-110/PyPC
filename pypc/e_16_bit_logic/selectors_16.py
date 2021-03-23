from pypc.a_primitives.nand import nand
from pypc.b_basic_logic.selectors import mux
from typing import Tuple

from pypc.pypc_typing import Bool2, Bool3

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


# nand gates used: 192
def mux_16_4way(selectors: Bool2, a: Bool16, b: Bool16, c: Bool16, d: Bool16) -> Bool16:
    """16 bit multiplexer which can choose from 4 inputs.
        
        returns a if selectors = False, False
        returns b if selectors = False, True
        returns c if selectors = True, False
        returns d if selectors = True, True
    """

    mux_ab = mux_16(selectors[0], a, b)
    mux_cd = mux_16(selectors[0], c, d)
    return mux_16(selectors[1], mux_ab, mux_cd)


# nand gates used: 448
def mux_16_8way(selectors: Bool3, a: Bool16, b: Bool16, c: Bool16, d: Bool16,
                e: Bool16, f: Bool16, g: Bool16, h: Bool16) -> Bool16:
    """16 bit multiplexer which can choose from 8 inputs.
    
        returns a if selectors = True, True, True
        returns b if selectors = False, True, True
        returns c if selectors = True, False, True
        returns d if selectors = False, False, True
        returns e if selectors = True, True, False
        returns f if selectors = False, True, False
        returns g if selectors = True, False, False
        returns h if selectors = False, False, False
    """
    mux_abcd = mux_16_4way(selectors[:2], a, b, c, d)
    mux_efgh = mux_16_4way(selectors[:2], e, f, g, h)
    return mux_16(selectors[2], mux_abcd, mux_efgh)
