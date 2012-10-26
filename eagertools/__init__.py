# Hoist functions up.
from eagertools.consume import consume
from eagertools.eager import eager_map as map
from eagertools.eager import domap, dostarmap, starmap

# Create some aliases in case people want to use the eager and lazy
# versions at the same time.
emap = map
estarmap = starmap
