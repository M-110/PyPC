from pypc.b_basic_logic.core_logic_gates import or_, not_, and_
from pypc.e_16_bit_logic.selectors_16 import mux_16
from pypc.f_16_bit_arithmetic.arithmetic_16 import inc_16
from pypc.g_16_bit_memory.register import register_16_bit_factory_clocked, register_16_bit_factory
from pypc.pypc_typing import Bool16


# TODO: Remove if clocked is unnecessary.
def pc_factory_clocked():
    state = (False,) * 16
    register = register_16_bit_factory_clocked()

    def pc(in_: Bool16, load: bool, inc: bool, reset: bool, clock: bool) -> Bool16:
        nonlocal state
        nonlocal register
        inc_out = inc_16(state)
        mux_inc = mux_16(inc, in_, inc_out)
        mux_reset = mux_16(reset, mux_inc, (False,) * 16)
        state = register(mux_reset, load, clock)
        return state

    return pc


# TODO: Update
# nand gates used: 272
def pc_factory():
    register = register_16_bit_factory()

    def pc(in_: Bool16 = (False,) * 16, load: bool = False, inc: bool = False, reset: bool = False) -> Bool16:
        nonlocal register
        not_load = not_(load)
        use_inc = and_(not_load, inc)
        inc_out = inc_16(register())
        mux_inc = mux_16(use_inc, inc_out, in_)
        mux_reset = mux_16(reset, (False,)*16, mux_inc)
        load_or_inc = or_(load, inc)
        load_or_inc_or_reset = or_(load_or_inc, reset)
        return register(mux_reset, load_or_inc_or_reset)

    return pc
