# Simply reuse some contents from itertools. This is for things like
# the infinite iterators which, of course, can have no eager
# counterpart.
import itertools

count = itertools.count
cycle = itertools.cycle
repeat = itertools.repeat

# Hoist functions up.
from eagertools.eager import eager_map as map
from eagertools.eager import starmap

# Create some aliases in case people want to use the eager and lazy
# versions at the same time.
emap = map
estarmap = starmap
