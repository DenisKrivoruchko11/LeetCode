# Design a max stack that supports push, pop, top, peekMax and popMax.
#   push(x)   - Push element x onto stack.
#   pop()     - Remove the element on top of the stack and return it.
#   top()     - Get the element on the top.
#   peekMax() - Retrieve the maximum element in the stack.
#   popMax()  - Retrieve the maximum element in the stack, and remove it.
#               If you find more than one maximum elements, only remove the top-most one.
# -1e7 <= x <= 1e7
# Number of operations won’t exceed 10000.
# The last four operations won’t be called when stack is empty.

class MaxStack:
    def __init__(self):
        self.values, self.index_max = [], -1

    def push(self, x: int) -> None:
        self.values.append(x)
        if self.index_max == -1 or x >= self.values[self.index_max]:
            self.index_max = len(self.values) - 1

    def pop(self) -> int:
        x = self.values.pop()
        if self.index_max == len(self.values):
            self.index_max = max(range(len(self.values)), key=lambda i: (self.values[i], i)) if self.values else -1
        return x

    def top(self) -> int:
        return self.values[-1]

    def peek_max(self) -> int:
        return self.values[self.index_max]

    def pop_max(self) -> int:
        x = self.values[self.index_max]
        self.values = self.values.pop(self.index_max)
        self.index_max = max(range(len(self.values)), key=lambda i: (self.values[i], i)) if self.values else -1
        return x
