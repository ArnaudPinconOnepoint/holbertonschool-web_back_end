""" documented the file """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """FIFO caching system."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.keys_order = []  # Keep track of the order of keys for LIFO.

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm.

        If the cache exceeds MAX_ITEMS, remove the last item added.
        """
        if key is None or item is None:
            return

        # If the key already exists, update its value and reorder
        if key in self.cache_data:
            self.cache_data[key] = item
            return

        # Add the new key-value pair
        self.cache_data[key] = item
        self.keys_order.append(key)

        # If the cache exceeds MAX_ITEMS, evict the first added key
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.keys_order.pop(-1)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Get an item by key.

        Return None if the key is None or does not exist in the cache.
        """
        return self.cache_data.get(key, None)
