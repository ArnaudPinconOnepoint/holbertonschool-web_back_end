#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching
    

class BasicCache(BaseCaching):
    """ Base cache class """

    def put(self, key, item):
        """ 
        Add an item to the cache.
        """
        if key is None or item is None:
            return
        # Store the item in the cache_data dictionary
        self.cache_data[key] = item


    def get(self, key):
        """ get """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
