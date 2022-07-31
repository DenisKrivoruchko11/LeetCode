from collections import OrderedDict

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
#   LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#   int get(int key) Return the value of the key if the key exists, otherwise return -1.
#   void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair
#   to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.


class LRUCache:
    def __init__(self, capacity: int):
        self.cap, self.vs = capacity, OrderedDict()

    def get(self, key: int) -> int:
        if key in self.vs:
            self.vs.move_to_end(key)
            return self.vs[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.vs and len(self.vs) == self.cap:
            self.vs.popitem(False)
        self.vs[key] = value
        self.vs.move_to_end(key)
