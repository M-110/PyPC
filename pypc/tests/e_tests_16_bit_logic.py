from pypc.e_16_bit_logic.core_logic_gates_16 import or_16, and_16, not_16
from pypc.e_16_bit_logic.selectors_16 import mux_16
import unittest
from random import randint


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestLogic16Gates(unittest.TestCase):
    def setUp(self):
        self.test_pair_arrays = zip(tuple(self._generate_random_bool_arrays() for _ in range(100)),
                                    tuple(self._generate_random_bool_arrays() for _ in range(100)))

    def py_and_16(self, bools_a, bools_b):
        return tuple(a and b for a, b in zip(bools_a, bools_b))

    def py_or_16(self, bools_a, bools_b):
        return tuple(a or b for a, b in zip(bools_a, bools_b))

    def py_not_16(self, bools):
        return tuple(not a for a in bools)

    def _generate_random_bool_arrays(self):
        return tuple(bool(randint(0, 1)) for _ in range(16))

    def test_and(self):
        for pair in self.test_pair_arrays:
            self.assertEqual(self.py_and_16(*pair), and_16(*pair))
            
    def test_or(self):
        for pair in self.test_pair_arrays:
            self.assertEqual(self.py_or_16(*pair), or_16(*pair))
            
    def test_not(self):
        for pair in self.test_pair_arrays:
            self.assertEqual(self.py_not_16(pair[0]), not_16(pair[0]))
    
    def test_mux(self):
        for a, b in self.test_pair_arrays:
            self.assertEqual(mux_16(True, a, b), a)
            self.assertEqual(mux_16(False, a, b), b)


run_tests(TestLogic16Gates)
