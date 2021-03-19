from pypc.a_primitives.nand import nand
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestNandGate(unittest.TestCase):
    def setUp(self):
        self.test_pairs = [
            (True, True),
            (True, False),
            (False, True),
            (False, False)]

    def test_nand(self):
        for a, b in self.test_pairs:
            self.assertEqual(nand(a, b), not (a and b))


run_tests(TestNandGate)
