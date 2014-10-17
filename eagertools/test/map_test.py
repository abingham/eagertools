import unittest

from eagertools import domap, map


def no_args():
    return 1


def one_arg(x):
    return x


def two_args(x, y):
    return (x, y)


class MapTest(unittest.TestCase):
    def test_no_args(self):
        x = map(no_args, [])
        self.assertEqual(x, [])

    def test_one_iter(self):
        x = map(one_arg, range(100))
        self.assertEqual(x, list(range(100)))

    def test_two_iters(self):
        x = map(two_args, range(100), range(100, 200))
        self.assertEqual(x, list(zip(range(100), range(100, 200))))

    def test_no_args_no_store(self):
        x = domap(no_args, [])
        self.assertEqual(x, None)

    def test_one_iter_no_store(self):
        x = domap(one_arg, range(100))
        self.assertEqual(x, None)

    def test_two_iters_no_store(self):
        x = domap(two_args, range(100), range(100, 200))
        self.assertEqual(x, None)
