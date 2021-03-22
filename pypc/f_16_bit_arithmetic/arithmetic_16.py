from pypc.c_basic_arithmetic.arithmetic import half_adder, full_adder
from typing import Tuple

Bool16 = Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]


# nand gates used: 140
def adder_16(a: Bool16, b: Bool16) -> Bool16:
    """Adds 16 bit integers together. Maximum result: 65,536."""
    carry, sum_1 = half_adder(a[0], b[0])
    carry, sum_2 = full_adder(a[1], b[1], carry)
    carry, sum_3 = full_adder(a[2], b[2], carry)
    carry, sum_4 = full_adder(a[3], b[3], carry)
    carry, sum_5 = full_adder(a[4], b[4], carry)
    carry, sum_6 = full_adder(a[5], b[5], carry)
    carry, sum_7 = full_adder(a[6], b[6], carry)
    carry, sum_8 = full_adder(a[7], b[7], carry)
    carry, sum_9 = full_adder(a[8], b[8], carry)
    carry, sum_10 = full_adder(a[9], b[9], carry)
    carry, sum_11 = full_adder(a[10], b[10], carry)
    carry, sum_12 = full_adder(a[11], b[11], carry)
    carry, sum_13 = full_adder(a[12], b[12], carry)
    carry, sum_14 = full_adder(a[13], b[13], carry)
    carry, sum_15 = full_adder(a[14], b[14], carry)
    carry, sum_16 = full_adder(a[15], b[15], carry)
    return (sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8,
            sum_9, sum_10, sum_11, sum_12, sum_13, sum_14, sum_15, sum_16)


def inc_16(in_: Bool16) -> Bool16:
    """Increases the input value by 1."""
    carry, sum_1 = half_adder(in_[0], True)
    carry, sum_2 = half_adder(in_[1], carry)
    carry, sum_3 = half_adder(in_[2], carry)
    carry, sum_4 = half_adder(in_[3], carry)
    carry, sum_5 = half_adder(in_[4], carry)
    carry, sum_6 = half_adder(in_[5], carry)
    carry, sum_7 = half_adder(in_[6], carry)
    carry, sum_8 = half_adder(in_[7], carry)
    carry, sum_9 = half_adder(in_[8], carry)
    carry, sum_10 = half_adder(in_[9], carry)
    carry, sum_11 = half_adder(in_[10], carry)
    carry, sum_12 = half_adder(in_[11], carry)
    carry, sum_13 = half_adder(in_[12], carry)
    carry, sum_14 = half_adder(in_[13], carry)
    carry, sum_15 = half_adder(in_[14], carry)
    carry, sum_16 = half_adder(in_[15], carry)
    return (sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8,
            sum_9, sum_10, sum_11, sum_12, sum_13, sum_14, sum_15, sum_16)