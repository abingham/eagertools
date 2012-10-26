import itertools
import unittest

from eagertools import starmap

def no_args():
    return 1

def two_args(x, y):
    return x + y

class StarmapTest(unittest.TestCase):
    def test_no_args(self):
        x = starmap(no_args, [])
        self.assertEqual(x, [])

    def test_two_iters(self):
        x = starmap(two_args, zip(range(100), range(100)))
        self.assertEqual(
            x,
            list(itertools.starmap(two_args,
                                   zip(range(100), range(100)))))

    def test_no_args_no_store(self):
        x = starmap(no_args, [], store=False)
        self.assertEqual(x, None)

    def test_two_iters(self):
        x = starmap(two_args, zip(range(100), range(100)), store=False)
        self.assertEqual(x, None)
