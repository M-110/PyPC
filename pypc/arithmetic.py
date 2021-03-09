from .nand import nand


def half_adder(a: bool, b: bool) -> (bool, bool):
    """Returns a + b in the form of a tuple of two bools representing the two
    bits."""
    nand_a_b = nand(a, b)
    nand_c = nand(nand_a_b, a)
    nand_d = nand(nand_a_b, b)
    high = nand(nand_a_b, nand_a_b)
    low = nand(nand_c, nand_d)
    return high, low, high
