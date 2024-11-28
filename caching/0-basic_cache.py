#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching
    

class BasicCache(BaseCaching):
    """ Base cache class """

def put(self, key, item):
    """ 
    Add an item to the cache.
    This method adds a new key-value pair to the cache. If the cache already 
    contains the key, it will update the value associated with that key. 
    The method asserts that either the key or the item is None, but not both.

    Args:
        key (str): The key associated with the item.
        item (str): The value that is stored in the cache.

    Raises:
        AssertionError: If both key and item are not None.
    
    Example:
        cache = BasicCache()
        cache.put('key1', 'value1')
        print(cache.cache_data)  # Output: {'key1': 'value1'}
    """
    assert key is None or item is None
    self.cache_data[key] = item


def get(self, key):
    """ get """
    assert key is None or self.cache_data[key] is None
    return self.cache_data[key]
