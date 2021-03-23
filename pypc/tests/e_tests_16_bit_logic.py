from itertools import product

from pypc.e_16_bit_logic.core_logic_gates_16 import or_16, and_16, not_16
from pypc.e_16_bit_logic.selectors_16 import mux_16, mux_16_4way, mux_16_8way
import unittest
from random import randint

from pypc.tests._converter import int_to_bool16


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestLogic16Gates(unittest.TestCase):
    def setUp(self):
        self.test_pair_arrays = zip(tuple(self._generate_random_bool_arrays() for _ in range(100)),
                                    tuple(self._generate_random_bool_arrays() for _ in range(100)))
        [-32768, -1, 0, 1, 32763, -21845, 21845, 10922, -10922]

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

    def test_mux_4way(self):
        a, b, c, d = [int_to_bool16(num) for num in [-21845, 21845, 10922, -10922]]
        for selectors in list(product([True, False], repeat=2)):
            out = mux_16_4way(selectors, a, b, c, d)

            if selectors[1]:
                if selectors[0]:
                    expected = a
                else:
                    expected = b
            else:
                if selectors[0]:
                    expected = c
                else:
                    expected = d
            self.assertEqual(expected, out)
            
    def test_mux_8way(self):
        a, b, c, d, e, f, g, h = [int_to_bool16(num) 
                                  for num in [-32768, -1, 0, 1,
                                              32763, -21845, 21845, 10922]]
        
        for selectors in list(product([True, False], repeat=3)):
            out = mux_16_8way(selectors, a, b, c, d, e, f, g, h)
            """
            returns a if selectors = True, True, True
            returns b if selectors = True, True, False
            returns c if selectors = True, False, True
            returns d if selectors = True, False, False
            returns e if selectors = False, True, True
            returns f if selectors = False, True, False
            returns g if selectors = False, False, True
            returns h if selectors = False, False, False
            """
            if selectors[2]:
                if selectors[1]:
                    if selectors[0]:
                        expected = a
                    else:
                        expected = b
                else:
                    if selectors[0]:
                        expected = c
                    else:
                        expected = d
            else:
                if selectors[1]:
                    if selectors[0]:
                        expected = e
                    else:
                        expected = f
                else:
                    if selectors[0]:
                        expected = g
                    else:
                        expected = h
            self.assertEqual(expected, out)
            


run_tests(TestLogic16Gates)
