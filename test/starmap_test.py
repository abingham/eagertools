import itertools

from eagertools import dostarmap, starmap
from hypothesis import given
import hypothesis.strategies as ST

from util import no_args, two_args


def test_no_args():
    assert starmap(no_args, []) == []


@given(ST.lists(ST.integers()), ST.lists(ST.integers()))
def test_two_iters(xs, ys):
    expected = list(itertools.starmap(two_args, zip(xs, ys)))
    actual = starmap(two_args, zip(xs, ys))
    assert actual == expected


def test_no_args_no_store():
    assert dostarmap(no_args, []) is None


@given(ST.lists(ST.integers()), ST.lists(ST.integers()))
def test_two_iters_no_store(xs, ys):
    assert dostarmap(two_args, zip(xs, ys)) is None
