import unittest

from eagertools import chain

class ChainTest(unittest.TestCase):
    def test_no_args(self):
        x = chain()
        self.assertEqual(x, [])

    def test_one_arg(self):
        x = chain(range(100))
        self.assertEqual(x, list(range(100)))

    def test_two_args(self):
        x = chain(range(100), range(300, 400))
        self.assertEqual(x, list(range(100)) + list(range(300, 400)))