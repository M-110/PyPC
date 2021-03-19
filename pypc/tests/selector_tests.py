from pypc.b_basic_logic.selectors import mux, demux
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestArithmetic(unittest.TestCase):
    def setUp(self):
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


run_tests(TestArithmetic)
