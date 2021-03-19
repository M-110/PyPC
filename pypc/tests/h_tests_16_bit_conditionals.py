import unittest
from pypc.pypc_typing import Bool16
from pypc.h_16_bit_conditionals.conditionals_16 import equal_to_zero, less_than_zero
from pypc.tests._converter import int_to_bool16

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestConditionals16(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [-32768, -1, 0, 1, 32767, -21845, 21845, 10922, -10922]

    def test_negative(self):
        for num in self.test_numbers:
            num_bool16 = int_to_bool16(num)
            self.assertEqual(num < 0, less_than_zero(num_bool16))

    def test_zero(self):
        for num in self.test_numbers:
            num_bool16 = int_to_bool16(num)
            self.assertEqual(num == 0, equal_to_zero(num_bool16))


run_tests(TestConditionals16)
