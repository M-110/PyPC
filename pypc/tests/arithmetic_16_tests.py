from pypc.f_16_bit_arithmetic.arithmetic_16 import adder_16
from pypc.g_16_bit_memory.register import register_16_bit_factory
from typing import Tuple
from random import randint
import unittest

Bool16 = Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestArithmetic16(unittest.TestCase):
    def setUp(self):
        self.a = register_16_bit_factory()
        self.b = register_16_bit_factory()
        self.values = ((randint(0, 32767), randint(0, 32767)) for _ in range(2000))

    def _int_to_bool16(self, num: int) -> Bool16:
        binary_string = bin(num)[2:].zfill(16)
        return tuple(True if char == '1' else False for char in binary_string)

    def _bool16_to_int(self, bools: Bool16) -> int:
        binary_string = ''.join(['1' if char else '0' for char in bools])
        return int(binary_string, 2)

    def _set_register_to_int(self, register, num: int):
        num_bool16 = self._int_to_bool16(num)
        register(num_bool16, True, False)
        register(clock=True)
        register(clock=False)

    def test_adder_16(self):
        for a, b in self.values:
            self._set_register_to_int(self.a, a)
            self._set_register_to_int(self.b, b)
            c_bools = adder_16(self.a(), self.b())
            c = self._bool16_to_int(c_bools)
            self.assertEqual(a + b, c)



run_tests(TestArithmetic16)
