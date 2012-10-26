import itertools

def eager_map(func, *iterables):
    """Calls a function using arguments from each of the
    iterables. Stops when the shortest iterable is exhausted.

    This is simply an eager version of the builtin ``map()``
    function. Since this is eager, it will run forever if any of the
    inputs is infinite.

    Args:
      func: The function to map over the inputs.
      iterables: Iterable objects used as input to ``func``.

    Returns: A list containing the results of mapping ``func`` over
      ``iterables``.

    """

    return list(map(func, *iterables))

def eager_chain(*iterables):
    """Return a list whose contents are all of the elements from the
    first iterable, then all of the elements from the next iterable,
    until all of the iterables are exhausted.

    This is simply an eager version of ``itertools.chain()``. Since
    this is eager, it will run forever if any of the iterables is
    infinite.

    Args:
      iterables: The iterable objects whose contents will be
        chained.

    Returns: A list containing all of the contents of the
      iterables.

    """

    return list(itertools.chain(*iterables))