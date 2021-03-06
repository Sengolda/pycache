from collections import OrderedDict, defaultdict

from .cache import Cache


class LFUCache(Cache):
    """
    Represents an LFU Cache.

    Args:
        capacity: A amount of total remains you want to have.
    """

    def __init__(self, capacity):
        self.remain = capacity
        self.least_freq = 1
        self.node_for_freq = defaultdict(OrderedDict)
        self.node_for_key = dict()
        super().__init__(self.node_for_freq)

    def _update(self, key, value):
        """
        Called whenever a key is fetched.
        """
        _, freq = self.node_for_key[key]
        self.node_for_freq[freq].pop(key)
        if len(self.node_for_freq[self.least_freq]) == 0:
            self.least_freq += 1
        self.node_for_freq[freq + 1][key] = (value, freq + 1)
        self.node_for_key[key] = (value, freq + 1)

    def get(self, key):
        """
        Get a key.
        Args:
            key: The key you want to fetch.
        """
        if key not in self.node_for_key:
            return None
        value = self.node_for_key[key][0]
        self._update(key, value)
        return value

    def put(self, key, value):
        """
        Put a key in the cache.
        Args:
            key: The key's name
            value: The key's value.
        """
        if key in self.node_for_key:
            self._update(key, value)
        else:
            self.node_for_key[key] = (value, 1)
            self.node_for_freq[1][key] = (value, 1)
            if self.remain == 0:
                removed = self.node_for_freq[self.least_freq].popitem(last=False)
                self.node_for_key.pop(removed[0])
            else:
                self.remain -= 1
                self.least_freq = 1
