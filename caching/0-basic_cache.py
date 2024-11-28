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
        assert key is None or item is None
        self.cache_data[key] = item


    def get(self, key):
        """ get """
        assert key is None or self.cache_data[key] is None
        return self.cache_data[key]
