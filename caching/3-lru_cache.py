""" documented the file """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.keys_order = []  # Keep track of the order of keys for LIFO.

    def put(self, key, item):
        """
        Add an item in the cache using LRU algorithm.

        If the cache exceeds MAX_ITEMS, remove the Least Recently Used item.
        """
        if key is None or item is None:
            return

        # If the key already exists, update its value and reorder
        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys_order.remove(key)
            self.keys_order.insert(0, key)
            return

        # Add the new key-value pair
        self.cache_data[key] = item
        self.keys_order.insert(0, key)

        # If the cache exceeds MAX_ITEMS, evict the LRU item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.keys_order.pop(-1)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Get an item by key.

        Return None if the key is None or does not exist in the cache.
        """
        if key in self.cache_data:
            self.keys_order.remove(key)
            self.keys_order.insert(0, key)
            return self.cache_data[key]
        return None
