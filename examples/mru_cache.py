from pycache import MRUCache

cache = MRUCache()
cache["foo"] = "a"
cache["foo1"] = "b"
cache["foo2"] = "c"

print(cache.cache)
print(cache["foo"])
