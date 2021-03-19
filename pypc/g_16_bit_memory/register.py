from pypc.d_basic_memory.memory import dff_factory
from typing import Tuple, Callable

Bool16 = Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]


# nand gates used: 144
def register_16_bit_factory() -> Callable:
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

    def register_16_bit(in_: Bool16 = (False,)*16, load: bool = False, clock: bool = False) -> Bool16:
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
