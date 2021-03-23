from pypc.b_basic_logic.selectors import demux_8way
from pypc.e_16_bit_logic.selectors_16 import mux_16_8way
from pypc.g_16_bit_memory.register import register_16_bit_factory
from pypc.pypc_typing import Bool3, Bool16

demux_8way()
mux_16_8way()
register_16_bit_factory()


# nand gates used: 995
def ram_8_factory():
    reg_a = register_16_bit_factory()
    reg_b = register_16_bit_factory()
    reg_c = register_16_bit_factory()
    reg_d = register_16_bit_factory()
    reg_e = register_16_bit_factory()
    reg_f = register_16_bit_factory()
    reg_g = register_16_bit_factory()
    reg_h = register_16_bit_factory()

    def ram_8(in_: Bool16, load: bool, address: Bool3):
        """Memory using 8 16-bit registers"""
        load_a, load_b, load_c, load_d, load_e, load_f, load_g, load_h = demux_8way(load, address)

        return mux_16_8way(address,
                           reg_a(in_, load_a),
                           reg_b(in_, load_b),
                           reg_c(in_, load_c),
                           reg_d(in_, load_d),
                           reg_e(in_, load_e),
                           reg_f(in_, load_f),
                           reg_g(in_, load_g),
                           reg_h(in_, load_h))
    return ram_8
