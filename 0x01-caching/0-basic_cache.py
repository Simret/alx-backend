#!/usr/bin/env python3
'''Basic caching module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''An object that allows storing and retrieving from a dictionary'''
    def put(self, key, item):
        '''Add item'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieve item'''
        return self.cache_data.get(key, None)
