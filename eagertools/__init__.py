# Hoist functions from their individual modules
from eagertools.map import eager_map as map

# Create some aliases in case people want to use the eager and lazy
# versions at the same time.
emap = map