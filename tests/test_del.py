import pycache
from pycache.lru import LRUCache

cache = LRUCache()
cache["e"] = "E"

del cache["e"]

print(cache.cache)
