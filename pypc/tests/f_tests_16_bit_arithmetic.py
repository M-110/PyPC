from pypc.f_16_bit_arithmetic.arithmetic_16 import adder_16, inc_16
from pypc.g_16_bit_memory.register import register_16_bit_factory_clocked
from typing import Tuple
from random import randint
import unittest

from pypc.tests._converter import int_to_bool16, bool16_to_int

Bool16 = Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestArithmetic16(unittest.TestCase):
    def setUp(self):
        self.a = register_16_bit_factory_clocked()
        self.b = register_16_bit_factory_clocked()
        self.values = ((-32767, 32766),
                       (-32768, 0),
                       (-32768, 1),
                       (0, 32767),
                       (-16232, 16232),
                       (-32767, -1),
                       (1, 32766),
                       (0, 0),
                       (-1, -1),
                       (1, 1),
                       (0, 1),
                       (0, -1),
                       (-1, 0),
                       )

    def _set_register_to_int(self, register, num: int):
        num_bool16 = int_to_bool16(num)
        register(num_bool16, True, False)
        register(clock=True)
        register(clock=False)

    def test_adder_16(self):
        # for a, b in self.values:
        for a, b in ((5, 25),):
            a_bools = int_to_bool16(a)
            b_bools = int_to_bool16(b)
            c_bools = adder_16(a_bools, b_bools)
            c = bool16_to_int(c_bools)
            self.assertEqual(a + b, c)

    def test_inc_16(self):
        for i in (0, 1, -1, -32767, 32765, -1632, 1632):
            i_plus_1 = int_to_bool16(i + 1)
            i = int_to_bool16(i)
            self.assertEqual(i_plus_1, inc_16(i))


run_tests(TestArithmetic16)
