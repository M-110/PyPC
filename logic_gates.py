from nand import nand

def not_(a: bool) -> bool:
    """Return not a."""
    return nand(a, a)

def and_(a: bool, b: bool) -> bool:
    """Return a and b."""
    nand_a_b = nand(a, b)
    return nand(nand_a_b, nand_a_b)

def or_(a: bool, b: bool) -> bool:
    """Return a or b."""
    not_a = nand(a, a)
    not_b = nand(b, b)
    return nand(not_a, not_b)

def xor_(a: bool, b: bool) -> bool:
    """Return a xor b."""
    nand_a_b = nand(a, b)
    nand_c = nand(nand_a_b, a)
    nand_d = nand(nand_a_b, b)
    return nand(nand_c, nand_d)


def run_tests():
    test_pairs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)]
    for a, b in test_pairs:
        assert (a and b) == and_(a, b)
        assert (a or b) == or_(a, b)
        assert ((a or b) and not (a and b)) == xor_(a, b)
    
    assert not_(True) == False
    assert not_(False) == True
    
    print('Tests passed')
    
run_tests()
    