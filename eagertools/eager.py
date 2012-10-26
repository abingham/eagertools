"""These are 'eager' versions of some of the itertools functions, as
well some related builtins. The original versions are 'lazy', meaning
that they only produce results as needed. This is often good, but
sometimes you really just want the algorithm to eagerly evaluate the
results without being prodded. That's what these functions are for.

IMPORTANT NOTE: Since these functions are eager, they will immediately
iterate over all inputs rather than waiting. This means that, if any
of your inputs are infinite or just very large, these functions will
never return and/or consume a lot of system resources. You have been
warned.

"""

import itertools

def eager_filter(func, iterable):
    """Return a list containing those items of ``iterable`` for which
    ``func(item)`` is true. If function is None, return the items that
    are true.

    """

    return list(filter(func, iterable))

def eager_map(func, *iterables):
    """Calls ``func`` using arguments from each of the
    ``iterables``. Stops when the shortest iterable is
    exhausted. Return a list of results.

    """

    return list(map(func, *iterables))

def chain(*iterables):
    """Return a list whose contents are all of the elements from the
    first iterable, then all of the elements from the next iterable,
    until all of the iterables are exhausted.

    """

    return list(itertools.chain(*iterables))

def compress(data, selectors):
    """Return a list of ``data`` elements corresponding to true
     ``selectors`` elements.  Forms a shorter list from selected
     ``data`` elements using the ``selectors`` to choose the data
     elements.

    """

    return list(itertools.compress(data, selectors))

def dropwhile(pred, seq):
    """Drop items from ``seq`` while ``predicate(item)`` is
      true. Returns a list of all items in ``seq`` after the predicate
      returns false.

    """

    return list(itertools.dropwhile(pred, seq))