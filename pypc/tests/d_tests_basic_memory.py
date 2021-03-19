from pypc.d_basic_memory.memory import latch_factory, dff_factory
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
        self.assertEqual(latch(False, False),
                         False)
        self.assertEqual(latch(True, False),
                         False)
        self.assertEqual(latch(True, True),
                         True)
        self.assertEqual(latch(False, True),
                         True)
        self.assertEqual(latch(False, False),
                         True)
        self.assertEqual(latch(True, False),
                         False)
        self.assertEqual(latch(False, False),
                         False)
        
    def test_dff(self):
        dff = dff_factory()
        self.assertEqual(dff(False, False, False),
                         False)
        self.assertEqual(dff(True, False, False),
                         False)
        self.assertEqual(dff(True, True, False),
                         False)
        self.assertEqual(dff(False, True, False),
                         False)
        self.assertEqual(dff(False, False, False),
                         False)
        self.assertEqual(dff(False, False, True),
                         True)
        self.assertEqual(dff(False, False, False),
                         True)
        self.assertEqual(dff(True, False, True),
                         True)
        self.assertEqual(dff(True, True, True),
                         True)
        self.assertEqual(dff(True, False, True),
                         True)
        self.assertEqual(dff(False, True, True),
                         True)
        self.assertEqual(dff(False, True, False),
                         True)
        self.assertEqual(dff(True, True, False),
                         True)
        self.assertEqual(dff(True, False, False),
                         True)
        self.assertEqual(dff(False, False, False),
                         True)
        self.assertEqual(dff(False, False, True),
                         False)
        self.assertEqual(dff(False, False, False),
                         False)


run_tests(TestMemory)
