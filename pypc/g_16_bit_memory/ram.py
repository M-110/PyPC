from pypc.b_basic_logic.selectors import demux_8way
from pypc.e_16_bit_logic.selectors_16 import mux_16_8way
from pypc.g_16_bit_memory.register import register_16_bit_factory
from pypc.pypc_typing import Bool3, Bool16


# demux8way = 35, mux8way16 = 448
# nand gates used: 995
from pypc_typing import Bool6


def ram_8_factory():
    reg_a = register_16_bit_factory()
    reg_b = register_16_bit_factory()
    reg_c = register_16_bit_factory()
    reg_d = register_16_bit_factory()
    reg_e = register_16_bit_factory()
    reg_f = register_16_bit_factory()
    reg_g = register_16_bit_factory()
    reg_h = register_16_bit_factory()

    def ram_8(in_: Bool16, load: bool, address: Bool3) -> Bool16:
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


# nand gates used: 8443
def ram_64_factory():
    ram_8_a = ram_8_factory()
    ram_8_b = ram_8_factory()
    ram_8_c = ram_8_factory()
    ram_8_d = ram_8_factory()
    ram_8_e = ram_8_factory()
    ram_8_f = ram_8_factory()
    ram_8_g = ram_8_factory()
    ram_8_h = ram_8_factory()
    
    def ram_64(in_: Bool16, load: bool, address: Bool6) -> Bool16:
        """Memory using 64 16-bit registers"""
        load_a, load_b, load_c, load_d, load_e, load_f, load_g, load_h = demux_8way(load, address[0:3])
        return mux_16_8way(address,
                           ram_8_a(in_, load_a, address[3:6]),
                           ram_8_b(in_, load_b, address[3:6]),
                           ram_8_c(in_, load_c, address[3:6]),
                           ram_8_d(in_, load_d, address[3:6]),
                           ram_8_e(in_, load_e, address[3:6]),
                           ram_8_f(in_, load_f, address[3:6]),
                           ram_8_g(in_, load_g, address[3:6]),
                           ram_8_h(in_, load_h, address[3:6]))
    return ram_64
