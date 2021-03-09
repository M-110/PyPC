from pypc.logic_gates import nand, not_, xor_, and_, or_
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestLogicGates(unittest.TestCase):
    def setUp(self):
        self.test_pairs = [
            (True, True),
            (True, False),
            (False, True),
            (False, False)]

    def test_logic(self):
        for a, b in self.test_pairs:
            self.assertEqual(nand(a, b), not(a and b))
            self.assertEqual(and_(a, b), a and b)
            self.assertEqual(or_(a, b), a or b)
            self.assertEqual(xor_(a, b), (a or b) and not (a and b))
            
    def test_not(self):
        self.assertEqual(not_(True), False)
        self.assertEqual(not_(False), True)
        

run_tests(TestLogicGates)
