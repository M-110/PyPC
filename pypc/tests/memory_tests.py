from pypc.memory import latch_factory, dff_factory
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestMemory(unittest.TestCase):
    def setUp(self):
        pass

    def test_latch(self):
        latch = latch_factory()
        self.assertEqual(latch(False, False), False)
        self.assertEqual(latch(True, False), False)
        self.assertEqual(latch(True, True), True)
        self.assertEqual(latch(False, True), True)
        self.assertEqual(latch(False, False), True)
        self.assertEqual(latch(True, False), False)
        self.assertEqual(latch(False, False), False)
        
    def test_dff(self):
        pass


run_tests(TestMemory)
