from typing import Callable
from random import randint
import unittest

from pypc.g_16_bit_memory.program_counter import pc_factory
from pypc.pypc_typing import Bool16
from pypc.g_16_bit_memory.register import register_16_bit_factory_clocked, register_16_bit_factory
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

    def test_register_clocked(self):
        register = register_16_bit_factory_clocked()
        for number in self.test_numbers:
            self._load_memory(register, number)
            return_number = self._read_memory(register)
            self.assertEqual(number, return_number)

    def test_register(self):
        register = register_16_bit_factory()
        for num in self.test_numbers:
            num_bool16 = int_to_bool16(num)
            self.assertEqual(register((False,) * 16, True),
                             (False,) * 16)
            self.assertEqual(register(num_bool16, False),
                             (False,) * 16)
            self.assertEqual(register(num_bool16, True),
                             num_bool16)
            self.assertEqual(register((False,) * 16, False),
                             num_bool16)

    def test_pc(self):
        pc = pc_factory()
        for num in [-32768, -1, 0, 1, 32763, -21845, 21845, 10922, -10922]:
            num_bool16 = int_to_bool16(num)
            num_plus_1 = int_to_bool16(num + 1)
            num_plus_2 = int_to_bool16(num + 2)
            num_plus_3 = int_to_bool16(num + 3)
            num_plus_4 = int_to_bool16(num + 4)
            # Reset to 0
            self.assertEqual(pc(reset=True),
                             (False,) * 16)
            # Input to num but don't load
            self.assertEqual(pc(in_=num_bool16),
                             (False,) * 16)
            # Load num
            self.assertEqual(pc(in_=num_bool16, load=True),
                             num_bool16)
            # Don't do anything to see if output remains the same
            self.assertEqual(pc(),
                             num_bool16)
            # Increase counter by 1
            self.assertEqual(pc(inc=True),
                             num_plus_1)
            # Increase counter by 1 and input unused number
            self.assertEqual(pc(in_=num_bool16, inc=True),
                             num_plus_2)
            # Increase counter by 1
            self.assertEqual(pc(inc=True),
                             num_plus_3)
            # Increase counter by 1 and input unused number
            self.assertEqual(pc(in_=num_bool16, inc=True),
                             num_plus_4)
            # Load num, increase counter, and reset
            self.assertEqual(pc(in_=num_bool16, load=True, inc=True, reset=True),
                             (False,) * 16)
            # Load num and increase counter
            self.assertEqual(pc(in_=num_bool16, load=True, inc=True),
                             num_bool16)
            # Increase num
            self.assertEqual(pc(inc=True),
                             num_plus_1)
            # Do nothing
            self.assertEqual(pc(),
                             num_plus_1)


run_tests(TestMemory16)
