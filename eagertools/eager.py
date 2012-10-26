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

def eager_map(func, *iterables, store=True):
    """Calls ``func`` using arguments from each of the
    ``iterables``. Stops when the shortest iterable is
    exhausted. Return a list of results.

    If ``store`` is False, then this simply consumes the results of
    the mapping.  In effect, this just calls the function for the
    inputs and nothing else.

    """

    processor = list if store else consume
    return processor(map(func, *iterables))

def starmap(func, seq, store=True):
    """Return an list whose values are returned from the function
    evaluated with a argument tuple taken from the given sequence.

    """

    processor = list if store else consume
    return processor(itertools.starmap(func, seq))