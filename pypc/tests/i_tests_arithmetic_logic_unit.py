import unittest
from itertools import product, combinations_with_replacement
from pypc.i_arithmetic_logic_unit.unary_alu import unary_alu
from pypc.f_16_bit_arithmetic.arithmetic_16 import adder_16
from pypc.i_arithmetic_logic_unit.alu import alu
from pypc.pypc_typing import Bool16
from pypc.tests._converter import int_to_bool16, bool16_to_int


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestALU(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [-32768, -1, 0, 1, 32767, -21845, 21845, 10922, -10922]
        self.test_pairs = list(combinations_with_replacement(self.test_numbers, 2))
        self.possible_params = list(product([True, False], repeat=6))

    def test_unary_alu(self):
        for num in self.test_numbers:
            num_bool16 = int_to_bool16(num)

            num_z = bool16_to_int(unary_alu(zero=True, negation=False, in_=num_bool16))
            num_n = bool16_to_int(unary_alu(zero=False, negation=True, in_=num_bool16))
            num_zn = bool16_to_int(unary_alu(zero=True, negation=True, in_=num_bool16))
            num_plain = bool16_to_int(unary_alu(zero=False, negation=False, in_=num_bool16))

            self.assertEqual(0, num_z)
            self.assertEqual(~num, num_n)
            self.assertEqual(~0, num_zn)
            self.assertEqual(num, num_plain)

    def py_alu(self, zx: bool, nx: bool, zy: bool, ny: bool, f: bool, no: bool, x: Bool16, y: Bool16) -> Bool16:
        """Python implementation of an ALU to use as a comparison."""
        if zx:
            x = (False,) * 16
        if zy:
            y = (False,) * 16
        if nx:
            x = tuple(not i for i in x)
        if ny:
            y = tuple(not i for i in y)
        if f:
            f_out = adder_16(x, y)
        else:
            f_out = tuple(x_i and y_i for x_i, y_i in zip(x, y))
        if no:
            return tuple(not i for i in f_out)
        else:
            return f_out

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
