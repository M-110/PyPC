from pypc.a_primitives.nand import nand
from typing import Callable


# nand gates used: 4
def latch_factory() -> Callable:
    """Created a latch function containing a closure that maintains
    the state in order to simulate sequential logic."""
    state = False

    def latch(store: bool, d: bool) -> bool:
        """If store is True, the latch output will be set to d, otherwise
        the previous output will be returned"""
        nonlocal state
        not_st = nand(store, store)
        nand_1 = nand(store, d)
        nand_2 = nand(not_st, state)
        state = nand(nand_1, nand_2)
        return state

    return latch


# TODO: Possibly remove if clock is deemed unnecessary.
# nand gates used: 9
def dff_factory() -> Callable:
    """Create a dff function containing a closure that maintains
    the two inner states in order to simulate sequential logic."""
    state_1 = False
    state_2 = False

    def dff(load: bool, in_: bool, clock: bool) -> bool:
        """A Data Flip-Flop component which stores and outputs a bit.
        
        The output only changes to the stored value when the clock
        changes from False to True.
        
        The stored value only changes when store is True.
        
        When clock is True, the store and d value do not change anything.
        """
        nonlocal state_1, state_2
        not_cl = nand(clock, clock)
        nand_1 = nand(load, not_cl)
        not_nand_1 = nand(nand_1, nand_1)
        nand_2 = nand(not_nand_1, in_)
        nand_3 = nand(nand_1, state_1)
        state_1 = nand(nand_2, nand_3)
        nand_5 = nand(clock, state_1)
        nand_6 = nand(not_cl, state_2)
        state_2 = nand(nand_5, nand_6)
        return state_2

    return dff


# nand gates used: 4
def bit_factory() -> Callable:
    """Created a bit component which stores its output.py
    
    If load is False, the bit will continue to output what
    it previously did.
    """
    state = False

    def bit(in_: bool, load: bool):
        nonlocal state
        not_load = nand(load, load)
        nand_1 = nand(in_, load)
        nand_2 = nand(not_load, state)
        state = nand(nand_1, nand_2)
        return state

    return bit
