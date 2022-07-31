import random

# Implement the RandomizedSet class:
#   RandomizedSet()      Initializes the RandomizedSet object.
#   bool insert(int val) Inserts an item val into the set if not present.
#                        Returns true if the item was not present, false otherwise.
#   bool remove(int val) Removes an item val from the set if present.
#                        Returns true if the item was present, false otherwise.
#   int getRandom()      Returns a random element from the current set of elements
#                        (it's guaranteed that at least one element exists when this method is called).
#                        Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.


class RandomizedSet:
    def __init__(self):
        self.vs_dict, self.vs_list = {}, []

    def insert(self, val: int) -> bool:
        if val not in self.vs_dict:
            self.vs_dict[val] = len(self.vs_list)
            self.vs_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.vs_dict:
            index, value = self.vs_dict.pop(val), self.vs_list.pop()
            if index < len(self.vs_list):
                self.vs_dict[value] = index
                self.vs_list[index] = value
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.vs_list)
