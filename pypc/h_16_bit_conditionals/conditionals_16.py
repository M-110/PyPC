from pypc.a_primitives.nand import nand
from pypc.b_basic_logic.core_logic_gates import or_, not_
from pypc.b_basic_logic.selectors import mux
from typing import Tuple
from pypc.typing import Bool16


# nand gates used: 46
def equal_to_zero(in_: Bool16) -> bool:
    """Returns True if in_ is equal to 0."""
    # Reduce to 8
    or_01 = or_(in_[0], in_[1])
    or_23 = or_(in_[2], in_[3])
    or_45 = or_(in_[4], in_[5])
    or_67 = or_(in_[6], in_[7])
    or_89 = or_(in_[8], in_[9])
    or_1011 = or_(in_[10], in_[11])
    or_1213 = or_(in_[12], in_[13])
    or_1415 = or_(in_[14], in_[15])
    # Reduce to 4
    or_0123 = or_(or_01, or_23)
    or_4567 = or_(or_45, or_67)
    or_891011 = or_(or_89, or_1011)
    or_12131415 = or_(or_1213, or_1415)
    # Reduce to 2
    or_01234567 = or_(or_0123, or_4567)
    or_89101112131415 = or_(or_891011, or_12131415)
    # Reduce to 1
    or_result = or_(or_01234567, or_89101112131415)
    # Return inverse
    return nand(or_result, or_result)
