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