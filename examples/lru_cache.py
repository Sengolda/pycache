from pycache import LRUCache

cache = LRUCache(128)
cache["foo"] = "a"
cache["foo1"] = "b"
cache["foo2"] = "c"

print(cache.cache)
print(cache["foo"])
