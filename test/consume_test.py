import unittest

from eagertools import consume


class ConsumeTest(unittest.TestCase):
    def test_consume_all(self):
        i = iter(range(100))
        consume(i)
        self.assertFalse(list(i))

    def test_consume_partial(self):
        i = iter(range(100))
        consume(i, n=50)
        self.assertListEqual(
            list(range(50, 100)),
            list(i))
