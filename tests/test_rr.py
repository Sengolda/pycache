from pycache import RRCache

cache = RRCache()
cache["e"] = "feel"

print(cache.popitem())
