from pypc.b_basic_logic.core_logic_gates import not_, xor_, and_, or_
from pypc.b_basic_logic.selectors import mux, demux
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestLogicGates(unittest.TestCase):
    def setUp(self):
        self.logic_pairs = [
            (True, True),
            (True, False),
            (False, True),
            (False, False)]

        self.mux_pairs = [
            ((False, False, False), False),
            ((False, True, False), False),
            ((False, False, True), True),
            ((False, True, True), True),
            ((True, False, False), False),
            ((True, False, True), False),
            ((True, True, False), True),
            ((True, True, True), True),
        ]

        self.demux_pairs = [
            ((False, False), (False, False)),
            ((False, True), (False, True)),
            ((True, False), (False, False)),
            ((True, True), (True, False)),
        ]

    def test_mux(self):
        for (sel, a, b), out in self.mux_pairs:
            self.assertEqual(mux(sel, a, b), out)

    def test_demux(self):
        for (sel, in_), (a, b) in self.demux_pairs:
            self.assertEqual(demux(sel, in_), (a, b))

    def test_logic(self):
        for a, b in self.logic_pairs:
            self.assertEqual(and_(a, b), a and b)
            self.assertEqual(or_(a, b), a or b)
            self.assertEqual(xor_(a, b), (a or b) and not (a and b))
            
    def test_not(self):
        self.assertEqual(not_(True), False)
        self.assertEqual(not_(False), True)
        

run_tests(TestLogicGates)
