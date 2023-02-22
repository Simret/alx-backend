#!/usr/bin/python3
'''FIFO caching'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A FIFO cache'''
    current_rank = 0

    def __init__(self):
        super().__init__()
        self.key_rank = {}

    def get_rank(self, order):
        '''Get the lowest/highest ranked key'''
        r = sorted(self.key_rank.items(), key=lambda x: x[1], reverse=order)
        return r[0][0]

    def put(self, key, item):
        '''Put item in the cache'''
        d = self.cache_data
        if key is not None and item is not None:
            if len(d) < BaseCaching.MAX_ITEMS or key in d:
                d.update({key: item})
                self.key_rank.update({key: FIFOCache.current_rank})
                FIFOCache.current_rank += 1
            else:
                rank = self.get_rank(False)
                d.pop(rank)
                self.key_rank.pop(rank)
                d.update({key: item})
                self.key_rank.update({key: FIFOCache.current_rank})
                FIFOCache.current_rank += 1
                print('DISCARD:', rank)

    def get(self, key):
        '''Get item from cache'''
        try:
            return self.cache_data[key]
        except Exception:
            return None
