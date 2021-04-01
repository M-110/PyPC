import unittest
from itertools import product, combinations_with_replacement
from typing import Tuple

from pypc.i_arithmetic_logic_unit.unary_alu import unary_alu
from pypc.f_16_bit_arithmetic.arithmetic_16 import adder_16
from pypc.i_arithmetic_logic_unit.alu import alu
from pypc.pypc_typing import Bool16
from pypc.tests._converter import int_to_bool16, bool16_to_int


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestCPU(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [-32768, -1, 0, 1, 32767, -21845, 21845, 10922, -10922]
        self.test_pairs = list(combinations_with_replacement(self.test_numbers, 2))
        self.possible_params = list(product([True, False], repeat=6))

    def test_alu(self):
        """2,880 combinations will be tested here. (9+8+7+6+5+4+3+2+1 * 2^6 = 2,880)"""
        for x, y in self.test_pairs:
            x = int_to_bool16(x)
            y = int_to_bool16(y)
            for params in self.possible_params:
                zx, nx, zy, ny, f, no = params
                expected = self.py_alu(zx, nx, zy, ny, f, no, x, y)
                alu_out = alu(zx, nx, zy, ny, f, no, x, y)
                self.assertEqual(alu_out, expected)


run_tests(TestALU)
