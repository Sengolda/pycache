import pycache
from pycache.lru import LRUCache

cache = LRUCache()
cache["e"] = "E"

print(cache.cache)
