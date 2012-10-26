import unittest

from eagertools import dropwhile

class DropwhileTest(unittest.TestCase):
    def test_empty(self):
        x = dropwhile(lambda x: True, [])
        self.assertEqual(x, [])

    def test_normal(self):
        x = dropwhile(lambda x: x < 10, range(100))
        self.assertEqual(x, list(range(10, 100)))