from pypc.c_basic_arithmetic.arithmetic import half_adder, full_adder
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.half_adder_pairs = [
            ((False, False), (False, False)),
            ((False, True), (False, True)),
            ((True, False), (False, True)),
            ((True, True), (True, False))
        ]
        
        self.full_adder_pairs = [
            ((False, False, False), (False, False)),
            ((False, False, True), (False, True)),
            ((False, True, False), (False, True)),
            ((False, True, True), (True, False)),
            ((True, False, False), (False, True)),
            ((True, False, True), (True, False)),
            ((True, True, False), (True, False)),
            ((True, True, True), (True, True)),
        ]

    def test_half_adder(self):
        for (a, b), (h, l) in self.half_adder_pairs:
            self.assertEqual(half_adder(a, b), (h, l))
            
    def test_full_adder(self):
        for (a, b, c), (h, l) in self.full_adder_pairs:
            self.assertEqual(full_adder(a, b, c), (h, l))
        

run_tests(TestArithmetic)
