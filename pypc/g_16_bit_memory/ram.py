from pypc.b_basic_logic.selectors import demux_8way, demux_4way
from pypc.e_16_bit_logic.selectors_16 import mux_16_8way, mux_16_4way
from pypc.g_16_bit_memory.register import register_16_bit_factory
from pypc.pypc_typing import Bool3, Bool16, Bool14, Bool6, Bool9, Bool12


# demux8way = 35, mux8way16 = 448
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


# nand gates used: 68027
def ram_512_factory():
    ram_64_a = ram_64_factory()
    ram_64_b = ram_64_factory()
    ram_64_c = ram_64_factory()
    ram_64_d = ram_64_factory()
    ram_64_e = ram_64_factory()
    ram_64_f = ram_64_factory()
    ram_64_g = ram_64_factory()
    ram_64_h = ram_64_factory()

    def ram_512(in_: Bool16, load: bool, address: Bool9) -> Bool16:
        """Memory using 512 16-bit registers."""
        load_a, load_b, load_c, load_d, load_e, load_f, load_g, load_h = demux_8way(load, address[0:3])
        return mux_16_8way(address,
                           ram_64_a(in_, load_a, address[3:9]),
                           ram_64_b(in_, load_b, address[3:9]),
                           ram_64_c(in_, load_c, address[3:9]),
                           ram_64_d(in_, load_d, address[3:9]),
                           ram_64_e(in_, load_e, address[3:9]),
                           ram_64_f(in_, load_f, address[3:9]),
                           ram_64_g(in_, load_g, address[3:9]),
                           ram_64_h(in_, load_h, address[3:9]))

    return ram_512


# nand gates used: 544699
def ram_4k_factory():
    ram_512_a = ram_512_factory()
    ram_512_b = ram_512_factory()
    ram_512_c = ram_512_factory()
    ram_512_d = ram_512_factory()
    ram_512_e = ram_512_factory()
    ram_512_f = ram_512_factory()
    ram_512_g = ram_512_factory()
    ram_512_h = ram_512_factory()

    def ram_4k(in_: Bool16, load: bool, address: Bool12) -> Bool16:
        """Memory using 4096 16-bit registers."""
        load_a, load_b, load_c, load_d, load_e, load_f, load_g, load_h = demux_8way(load, address[0:3])
        return mux_16_8way(address,
                           ram_512_a(in_, load_a, address[3:12]),
                           ram_512_b(in_, load_b, address[3:12]),
                           ram_512_c(in_, load_c, address[3:12]),
                           ram_512_d(in_, load_d, address[3:12]),
                           ram_512_e(in_, load_e, address[3:12]),
                           ram_512_f(in_, load_f, address[3:12]),
                           ram_512_g(in_, load_g, address[3:12]),
                           ram_512_h(in_, load_h, address[3:12]))

    return ram_4k


# nand gates used: 2179003
def ram_16k_factory():
    ram_4k_a = ram_4k_factory()
    ram_4k_b = ram_4k_factory()
    ram_4k_c = ram_4k_factory()
    ram_4k_d = ram_4k_factory()

    def ram_16k(in_: Bool16, load: bool, address: Bool14) -> Bool16:
        """Memory using 16,384 16-bit registers."""
        load_a, load_b, load_c, load_d = demux_4way(load, address[0:2])
        return mux_16_4way(address,
                           ram_4k_a(in_, load_a, address[2:14]),
                           ram_4k_b(in_, load_b, address[2:14]),
                           ram_4k_c(in_, load_c, address[2:14]),
                           ram_4k_d(in_, load_d, address[2:14]))

    return ram_16k
