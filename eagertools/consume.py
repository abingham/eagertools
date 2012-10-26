import collections

def consume(iterator, n=None):
    """Advance the iterator n-steps ahead. If n is none, consume entirely.

    Taken from Python's `iterools` documentation:

      http://docs.python.org/library/itertools.html#recipes

    """

    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)