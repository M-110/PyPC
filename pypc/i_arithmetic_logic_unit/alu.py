from pypc.pypc_typing import Bool16
from pypc.e_16_bit_logic.selectors_16 import mux_16
from pypc.e_16_bit_logic.core_logic_gates_16 import not_16
from pypc.f_16_bit_arithmetic.arithmetic_16 import adder_16
from pypc.e_16_bit_logic.core_logic_gates_16 import and_16
from pypc.i_arithmetic_logic_unit.unary_alu import unary_alu


def alu(zero_x: bool, negate_x: bool, zero_y: bool, negate_y: bool,
        add_x_y: bool, negate_output: bool, x: Bool16, y: Bool16) -> Bool16:
    unary_x = unary_alu(zero_x, negate_x, x)
    unary_y = unary_alu(zero_y, negate_y, y)
    x_add_y = adder_16(unary_x, unary_y)
    x_and_y = and_16(unary_x, unary_y)
    mux_add_and = mux_16(add_x_y, x_add_y, x_and_y)
    negated_out = not_16(mux_add_and)
    return mux_16(negate_output, negated_out, mux_add_and)
