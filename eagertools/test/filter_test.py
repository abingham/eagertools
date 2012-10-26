import unittest

from eagertools import filter

class DropwhileTest(unittest.TestCase):
    def test_empty_func(self):
        x = filter(lambda x: True, [])
        self.assertEqual(x, [])

    def test_empty_none(self):
        x = filter(None, [])
        self.assertEqual(x, [])

    def test_contents_func(self):
        x = filter(lambda x: x % 2, range(10))
        self.assertEqual(x, list(range(1,10,2)))

    def test_contents_none(self):
        x = filter(None, range(10))
        self.assertEqual(x, list(range(1, 10)))