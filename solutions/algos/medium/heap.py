import random


class Heap:
    def __init__(self, val=None):
        self.val = val
        self.left = self.right = None


def union(h1: Heap, h2: Heap) -> Heap:
    if h1.val is None or h2.val is None:
        return h1 if h2.val is None else h2
    elif h1.val > h2.val:
        return union(h2, h1)
    else:
        if random.randint(0, 1):
            h1.left = union(h1.left, h2)
        else:
            h1.right = union(h1.right, h2)
        return h1
