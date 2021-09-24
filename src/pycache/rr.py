from .cache import Cache
import random


class RRCache(Cache):
    """
    Represents an RR Cache.
    """

    def __init__(self):
        super().__init__(dict())
        self.__choice = random.choice

    @property
    def choice(self):
        return self.__choice

    def popitem(self):
        """
        Get a random item from the cache.
        """
        try:
            key = self.choice(list(self))
        except IndexError:
            raise KeyError(f"{self.__class__.__name__} is empty") from None
        else:
            return (key, self[key])
