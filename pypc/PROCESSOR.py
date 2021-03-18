from pypc.register import register_16_bit_factory
from pypc.arithmetic_16 import adder_16



def binary_to_int(reg):
    binary = reg((False,) * 16, False, False)
    binary = ''.join([str(int(b)) for b in binary])
    return int(binary, 2)
    
def int_to_bits(num):
    bits = register_16_bit_factory()
    bits_str = bin(num)[2:].zfill(16)
    bits_bool = [True if bit == '1' else 0 for bit in bits_str]
    bits(bits_bool, True, False)
    bits(bits_bool, True, True)
    return bits
    
if __name__ == "__main__":

    a = [True if a == '1' else False for a in '0000000000000001']
    b = [True if a == '1' else False for a in '0000000000000001']

    c = adder_16(a, b)
    c = ''.join(['1' if x else '0' for x in c])
    print(c)
    a = int_to_bits(32768)
    print('a', binary_to_int(a))
    b = int_to_bits(32767)
    
    print('b', binary_to_int(b))
    c = adder_16(a(), b())
    
    c_bits = register_16_bit_factory()
    
    c_bits(c, True, False)
    c_bits(c, True, True)
    output = binary_to_int(c_bits)
    
    print(output)
    print('a', a())
    print('b', b())
    print('c', c_bits())
    print('real c', c)
