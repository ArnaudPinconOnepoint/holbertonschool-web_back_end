#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching
    

class BasicCache(BaseCaching):
    """ Base cache class """

    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ 
        Add an item to the cache.
        """
        assert key is None or item is None
        self.cache_data[key] = item


    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def get(self, key):
        """ get """
        assert key is None or self.cache_data[key] is None
        return self.cache_data[key]
