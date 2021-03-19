from pypc.g_16_bit_memory.register import register_16_bit_factory
from pypc.f_16_bit_arithmetic.arithmetic_16 import adder_16
from pypc.tests._converter import int_to_bool16, bool16_to_int


a = int_to_bool16(1)
b = int_to_bool16(-1)
    
if __name__ == "__main__":
    print(a)
    print(b)
    c = adder_16(a, b)
    print(c)
