from typing import Callable
from random import randint
import unittest
from pypc.pypc_typing import Bool16
from pypc.g_16_bit_memory.register import register_16_bit_factory


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestMemory16(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [0, 65535, 1, 65534, 444, 34333, 20000, 16]

    def _int_to_bool16(self, num: int) -> Bool16:
        binary_string = bin(num)[2:].zfill(16)
        return tuple(True if char == '1' else False for char in binary_string)

    def _bool16_to_int(self, bools: Bool16) -> int:
        binary_string = ''.join(['1' if char else '0' for char in bools])
        return int(binary_string, 2)

    def _load_memory(self, register: Callable, num: int):
        num_bool16 = self._int_to_bool16(num)
        register(in_=num_bool16, load=True, clock=False)
        register(clock=True)
        register(clock=False)

    def _read_memory(self, register: Callable) -> int:
        output = register(clock=True)
        register(clock=False)
        return self._bool16_to_int(output)

    def test_register(self):
        register = register_16_bit_factory()
        for number in self.test_numbers:
            self._load_memory(register, number)
            return_number = self._read_memory(register)
            self.assertEqual(number, return_number)


run_tests(TestMemory16)
