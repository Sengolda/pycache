from collections import OrderedDict

from .cache import Cache


class LRUCache(Cache):
    """
    Represents an LRU Cache.

    Args:
        capacity: A amount of total remains you want to have. Defaults to 128.
    """
    def __init__(self, capacity: int = 128) -> None:
        self.cache = OrderedDict()
        self.capacity = capacity
        super().__init__(self.cache)

    def get(self, key):
        """
        Get a key.
        Args:
            key: The key you want to fetch.
        """
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value) -> None:
        """
        Put a key in the cache.
        Args:
            key: The key's name
            value: The key's value.
        """
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def pop(self, key, default=...):
        try:
            pop_item = self.cache.pop(str(key))
        except Exception as e:
            if default is ...:
                raise e
            else:
                return default
        else:
            return pop_item

    def popitem(self):
        try:
            key = next(iter(self.cache))
        except StopIteration:
            raise TypeError(f"{self.__class__.__name__} is empty") from None
        else:
            return (key, self.pop(key))
