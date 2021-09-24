from collections import OrderedDict

from .cache import Cache


class MRUCache(Cache):
    """
    Represents an MRU Cache.
    """
    def __init__(self):
        self.__order = OrderedDict()
        super().__init__(self, self.__order)

    def __getitem__(self, key):
        value = super().__getitem__(key=key)
        if key in self:
            self.__update(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.__update(key)

    def __delitem__(self, key):
        super().__setitem__(key)
        del self.__order[key]

    def popitem(self):
        try:
            key = next(iter(self.__order))
        except StopIteration:
            raise KeyError(f"{self.__class__.__name__} is empty") from None
        else:
            return (key, self.pop(key))

    def __update(self, key):
        """
        Called whanever the cache is updated.
        """
        try:
            self.__order.move_to_end(key, last=False)
        except KeyError:
            self.__order[key] = None
