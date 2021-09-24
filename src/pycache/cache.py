class DefaultSize:
    def __getitem__(self, _):
        return 1

    def __setitem__(self, _, value):
        assert value == 1

    def pop(self, _):
        return 1


class Cache:
    def __init__(self, cache):
        self.cache = cache
        self.__size = DefaultSize()

    def __getitem__(self, key):
        try:
            return self.cache[key]
        except KeyError:
            return self.__missing__(key)

    def __repr__(self) -> str:
        try:
            return f"{self.__class__.__name__} (currentsize={len(self.cache.items())})"
        except AttributeError:
            return f"<{self.__class__.__name__}>"

    def __contains__(self, key):
        return key in self.__data

    def __missing__(self, key):
        raise KeyError(key)

    def __iter__(self):
        return iter(self.cache)

    def __len__(self):
        return len(self.cache)

    def __setitem__(self, key, value):
        size = self.getsizeof(value)

        if key in self.cache:
            _size = size - self.__size[key]
        else:
            _size = size
            self.__size[key] = _size
            self.cache[key] = value

    def pop(self, key, default=...):
        try:
            self.cache.pop(key)
        except Exception as e:
            if default is ...:
                raise e
            else:
                return default
        else:
            return None

    def setdefault(self, key, default=None):
        if key in self:
            value = self[key]
        else:
            self[key] = value = default
        return value

    def getsizeof(self, _):
        return 1
