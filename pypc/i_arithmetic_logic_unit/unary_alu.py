from pypc.pypc_typing import Bool16
from pypc.e_16_bit_logic.selectors_16 import mux_16
from pypc.e_16_bit_logic.core_logic_gates_16 import not_16
from pypc.h_16_bit_conditionals.conditionals_16 import less_than_zero, equal_to_zero


def unary_alu(zero: bool, negation: bool, in_: Bool16) -> Bool16:
    """A unary arithmetic logic unit which can optionally zero the input
    or negate the output.

    Negation occurs after zeroing so if both are true, output will be -1.
    """
    mux_zero = mux_16(zero, (False,)*16, in_)
    mux_zero_negated = not_16(mux_zero)
    return mux_16(negation, mux_zero_negated, mux_zero)
