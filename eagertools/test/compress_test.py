import unittest

from eagertools import compress

class CompressTest(unittest.TestCase):
    def test_all_true(self):
        x = compress(range(100), (True for _ in range(100)))
        self.assertEqual(x, list(range(100)))

    def test_all_false(self):
        x = compress(range(100), (False for _ in range(100)))
        self.assertEqual(x, [])

    def test_mixed(self):
        def is_odd(i):
            return i % 2

        x = compress(range(100), (is_odd(i) for i in range(100)))
        self.assertEqual(x, list(range(1, 100, 2)))