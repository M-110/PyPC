from typing import Callable
from random import randint
import unittest
from pypc.pypc_typing import Bool16
from pypc.g_16_bit_memory.register import register_16_bit_factory
from pypc.tests._converter import bool16_to_int, int_to_bool16


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestMemory16(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [-32768, -1, 0, 1, 32767, -21845, 21845, 10922, -10922]

    def _load_memory(self, register: Callable, num: int):
        num_bool16 = int_to_bool16(num)
        register(in_=num_bool16, load=True, clock=False)
        register(clock=True)
        register(clock=False)

    def _read_memory(self, register: Callable) -> int:
        output = register(clock=True)
        register(clock=False)
        return bool16_to_int(output)

    def test_register(self):
        register = register_16_bit_factory()
        for number in self.test_numbers:
            self._load_memory(register, number)
            return_number = self._read_memory(register)
            self.assertEqual(number, return_number)


run_tests(TestMemory16)
