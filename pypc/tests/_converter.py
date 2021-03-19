from pypc.pypc_typing import Bool16


def int_to_bool16(num: int) -> Bool16:
    if num < 0:
        num += 32768
        binary_string = '1' + bin(num)[2:].zfill(15)
    else:
        binary_string = bin(num)[2:].zfill(16)
    return tuple(True if char == '1' else False for char in binary_string)


def bool16_to_int(bools: Bool16) -> int:
    binary_string = ''.join(['1' if char else '0' for char in bools[1:]])
    output = int(binary_string, 2)
    if bools[0]:
        output -= 32768
    return output
