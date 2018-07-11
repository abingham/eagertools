from eagertools import domap, emap
from hypothesis import given
import hypothesis.strategies as ST

from util import no_args, one_arg, two_args


def test_empty_input():
    assert emap(no_args, []) == []


@given(ST.lists(ST.integers()))
def test_one_iter(vals):
    assert emap(one_arg, vals) == list(map(one_arg, vals))


@given(ST.lists(ST.integers()), ST.lists(ST.integers()))
def test_two_iters(xs, ys):
    assert emap(two_args, xs, ys) == list(map(two_args, xs, ys))


def test_domap_does_not_call_func_for_empty_input():
    assert domap(no_args, []) is None


@given(ST.lists(ST.integers()))
def test_domap_gives_none_for_unary_function(vals):
    assert domap(one_arg, vals) is None


@given(ST.lists(ST.integers()), ST.lists(ST.integers()))
def test_domap_gives_none_for_binary_function(xs, ys):
    assert domap(two_args, xs, ys) is None
