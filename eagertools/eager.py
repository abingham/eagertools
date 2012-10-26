import itertools

def eager_map(func, *iterables):
    """Calls a function using arguments from each of the
    iterables. Stops when the shortest iterable is exhausted.

    This is an eager version of the builtin ``map()`` function. Since
    this is eager, it will run forever if any of the inputs is
    infinite.

    Args:
      func: The function to map over the inputs.
      iterables: Iterable objects used as input to ``func``.

    Returns: A list containing the results of mapping ``func`` over
      ``iterables``.

    """

    return list(map(func, *iterables))

def chain(*iterables):
    """Return a list whose contents are all of the elements from the
    first iterable, then all of the elements from the next iterable,
    until all of the iterables are exhausted.

    This is an eager version of ``itertools.chain()``. Since this is
    eager, it will run forever if any of the iterables is infinite.

    Args:
      iterables: The iterable objects whose contents will be
        chained.

    Returns: A list containing all of the contents of the
      iterables.

    """

    return list(itertools.chain(*iterables))

def compress(data, selectors):
    """Return a list of data elements corresponding to true selector
     elements.  Forms a shorter list from selected data elements
     using the selectors to choose the data elements.

    This is an eager version of ``itertools.compress()``. Since this
    is eager, it will run forever if any of the input is
    infinite.

    Args:
      data: The iterable from which this selects values.
      selectors: An iterable of booleans determining which values from
        ``data`` to select.

    Returns: A list containing the selected elements.

    """

    return list(itertools.compress(data, selectors))