from pypc.arithmetic import half_adder, full_adder
from typing import List, Tuple

Bool16 = Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]


def adder_16(a: Bool16, b: Bool16) -> Bool16:
    sum_1, carry = half_adder(a[0], b[0])
    sum_2, carry = full_adder(a[1], b[1], carry)
    sum_3, carry = full_adder(a[2], b[2], carry)
    sum_4, carry = full_adder(a[3], b[3], carry)
    sum_5, carry = full_adder(a[4], b[4], carry)
    sum_6, carry = full_adder(a[5], b[5], carry)
    sum_7, carry = full_adder(a[6], b[6], carry)
    sum_8, carry = full_adder(a[7], b[7], carry)
    sum_9, carry = full_adder(a[8], b[8], carry)
    sum_10, carry = full_adder(a[9], b[9], carry)
    sum_11, carry = full_adder(a[10], b[10], carry)
    sum_12, carry = full_adder(a[11], b[11], carry)
    sum_13, carry = full_adder(a[12], b[12], carry)
    sum_14, carry = full_adder(a[13], b[13], carry)
    sum_15, carry = full_adder(a[14], b[14], carry)
    sum_16, _ = full_adder(a[15], b[15], carry)
    return (sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7,
            sum_8, sum_9, sum_10, sum_11, sum_12, sum_13, sum_14, sum_15, sum_16)
