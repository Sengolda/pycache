from pycache import RRCache

cache = RRCache()
cache["foo"] = "abc"
cache["foo1"] = "cba"

print(cache.popitem())
