import unittest
from pypc.i_arithmetic_logic_unit.unary_alu import unary_alu
from pypc.tests._converter import int_to_bool16, bool16_to_int


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestALU(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [-32768, -1, 0, 1, 32767, -21845, 21845, 10922, -10922]

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


run_tests(TestALU)
