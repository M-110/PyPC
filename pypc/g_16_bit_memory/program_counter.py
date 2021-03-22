from pypc.e_16_bit_logic.selectors_16 import mux_16
from pypc.f_16_bit_arithmetic.arithmetic_16 import inc_16
from pypc.g_16_bit_memory.register import register_16_bit_factory
from pypc.pypc_typing import Bool16


def pc_factory():
    state = (False,) * 16
    register = register_16_bit_factory()
    
    def pc(in_: Bool16, load: bool, inc: bool, reset: bool, clock: bool) -> Bool16:
        nonlocal state
        nonlocal register
        inc_out = inc_16(state)
        mux_inc = mux_16(inc, in_, inc_out)
        mux_reset = mux_16(reset, mux_inc, (False,) * 16)
        state = register(mux_reset, load, clock)
        return state
    return pc
