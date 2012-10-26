# Hoist functions up.
from eagertools.eager import eager_filter as filter
from eagertools.eager import eager_map as map
from eagertools.eager import chain, compress, dropwhile

# Create some aliases in case people want to use the eager and lazy
# versions at the same time.
emap = map
echain = chain
ecompress = compress
edropwhile = dropwhile