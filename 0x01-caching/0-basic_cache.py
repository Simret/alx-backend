#!/usr/bin/env python3
'''Basic caching module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Cache'''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Put item'''
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        '''Get item'''
        try:
            return self.cache_data[key]
        except Exception:
            return None
