#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Base cache class """

    def __init__(self):
        """
        Initialization of FIFO Cache
        """
        super().__init__()


    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is None or item is None:
            return
        # Store the item in the cache_data dictionary
        if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print(f"DISCARD:\n{oldest_key}")
        self.cache_data[key] = item


    def get(self, key):
        """
        Get an item with a key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
