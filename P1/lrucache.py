from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.memory = OrderedDict()

    def get(self, key):
        # mark the element as MRU
        if key not in self.memory:
            return -1
        value = self.memory.pop(key)
        self.memory[key] = value
        return value

    def set(self, key, value):
        if len(self.memory) ==  self.capacity:
            # clear LRU slot
            self.memory.popitem(False)
        self.memory[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1

def test_lru():
    cache = LRU_Cache(3)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    assert cache.get(2) == 2
    cache.set(4, 4) # add 4 remove 1
    assert cache.get(1) == -1
    cache.set(5, 5) # add 5 remove 3
    assert cache.get(3) == -1
    assert cache.get(4) == 4

test_lru()
