from pypc.d_basic_memory.memory import dff_factory, bit_factory
from typing import Tuple, Callable

Bool16 = Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]


# TODO: Remove if clock is unnecessary.
# nand gates used: 144
def register_16_bit_factory_clocked() -> Callable[[Bool16, bool, bool], Bool16]:
    bit_1 = dff_factory()
    bit_2 = dff_factory()
    bit_3 = dff_factory()
    bit_4 = dff_factory()
    bit_5 = dff_factory()
    bit_6 = dff_factory()
    bit_7 = dff_factory()
    bit_8 = dff_factory()
    bit_9 = dff_factory()
    bit_10 = dff_factory()
    bit_11 = dff_factory()
    bit_12 = dff_factory()
    bit_13 = dff_factory()
    bit_14 = dff_factory()
    bit_15 = dff_factory()
    bit_16 = dff_factory()

    def register_16_bit(in_: Bool16 = (False,) * 16, load: bool = False, clock: bool = False) -> Bool16:
        return (bit_1(load, in_[0], clock),
                bit_2(load, in_[1], clock),
                bit_3(load, in_[2], clock),
                bit_4(load, in_[3], clock),
                bit_5(load, in_[4], clock),
                bit_6(load, in_[5], clock),
                bit_7(load, in_[6], clock),
                bit_8(load, in_[7], clock),
                bit_9(load, in_[8], clock),
                bit_10(load, in_[9], clock),
                bit_11(load, in_[10], clock),
                bit_12(load, in_[11], clock),
                bit_13(load, in_[12], clock),
                bit_14(load, in_[13], clock),
                bit_15(load, in_[14], clock),
                bit_16(load, in_[15], clock))

    return register_16_bit


# nand gates used: 64
def register_16_bit_factory() -> Callable:
    bit_1 = bit_factory()
    bit_2 = bit_factory()
    bit_3 = bit_factory()
    bit_4 = bit_factory()
    bit_5 = bit_factory()
    bit_6 = bit_factory()
    bit_7 = bit_factory()
    bit_8 = bit_factory()
    bit_9 = bit_factory()
    bit_10 = bit_factory()
    bit_11 = bit_factory()
    bit_12 = bit_factory()
    bit_13 = bit_factory()
    bit_14 = bit_factory()
    bit_15 = bit_factory()
    bit_16 = bit_factory()

    def register_16_bit(in_: Bool16 = (False,)*16, load: bool = False) -> Bool16:
        return (bit_1(in_[0], load),
                bit_2(in_[1], load),
                bit_3(in_[2], load),
                bit_4(in_[3], load),
                bit_5(in_[4], load),
                bit_6(in_[5], load),
                bit_7(in_[6], load),
                bit_8(in_[7], load),
                bit_9(in_[8], load),
                bit_10(in_[9], load),
                bit_11(in_[10], load),
                bit_12(in_[11], load),
                bit_13(in_[12], load),
                bit_14(in_[13], load),
                bit_15(in_[14], load),
                bit_16(in_[15], load))

    return register_16_bit
