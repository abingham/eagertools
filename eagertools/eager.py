"""These are 'eager' versions of some of the iterator-based
functions. The original versions are 'lazy', meaning that they only
produce results as needed. This is often good, but sometimes you
really just want the algorithm to eagerly evaluate the results without
being prodded. That's what these functions are for.

IMPORTANT NOTE: Since these functions are eager, they will immediately
iterate over all inputs rather than waiting. This means that, if any
of your inputs are infinite or just very large, these functions will
never return and/or consume a lot of system resources. You have been
warned.

"""

import itertools

from eagertools.consume import consume


def eager_map(func, *iterables):
    """Calls ``func`` using arguments from each of the
    ``iterables``. Stops when the shortest iterable is
    exhausted. Return a list of results.

    """

    return list(map(func, *iterables))


def domap(func, *iterables):
    """Calls ``func`` using arguments from each of the
    ``iterables``. Stops when the shortest iterable is exhausted. The
    results of the calls to ``func`` are not kept.

    """

    consume(map(func, *iterables))


def starmap(func, seq, store=True):
    """Return an list whose values are returned from the function
    evaluated with a argument tuple taken from the given sequence.

    """

    return list(itertools.starmap(func, seq))


def dostarmap(func, seq):
    """Apply a ``func`` to arguments taken from tuples in ``seq``."""

    consume(itertools.starmap(func, seq))
