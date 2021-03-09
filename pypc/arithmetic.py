from .nand import nand


def half_adder(a: bool, b: bool) -> (bool, bool):
    """Returns a + b in the form of a tuple of two bools representing the two
    bits."""
    nand_a_b = nand(a, b)
    nand_c = nand(nand_a_b, a)
    nand_d = nand(nand_a_b, b)
    high = nand(nand_a_b, nand_a_b)
    low = nand(nand_c, nand_d)
    return high, low


def full_adder(a: bool, b: bool, c: bool) -> (bool, bool):
    """Returns a + b + c in the form of a tuple of two bools representing the two
    bits.
    
    Carried value is ignored.
    """
    nand_a_b = nand(a, b)
    nand_c = nand(nand_a_b, a)
    nand_d = nand(nand_a_b, b)
    low_a_b = nand(nand_c, nand_d)
    nand_low_a_b_c = nand(low_a_b, c)
    nand_e = nand(low_a_b, nand_low_a_b_c)
    nand_f = nand(nand_low_a_b_c, c)
    high = nand(nand_a_b, nand_low_a_b_c)
    low = nand(nand_e, nand_f)
    return high, low
