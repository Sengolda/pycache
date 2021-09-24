class Cache:
    def __init__(self, cache):
        self.cache = cache
    


    def __repr__(self) -> str:
        try:
            return f"{self.__class__.__name__} (currentsize={len(self.cache.items())}"
        except AttributeError:
            return f"<{self.__class__.__name__}>"