from typing import Optional


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.stack[-1][1]) if self.stack else x))

    def pop(self) -> Optional[int]:
        return self.stack.pop()[0] if self.stack else None

    def get_min(self) -> Optional[int]:
        return self.stack[-1][1] if self.stack else None

    def empty(self) -> bool:
        return not self.stack


class MinQueue:
    def __init__(self):
        self.s1 = MinStack()
        self.s2 = MinStack()

    def put(self, x: int) -> None:
        self.s1.push(x)

    def get(self) -> Optional[int]:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop() if self.s2 else None

    def get_min(self) -> Optional[int]:
        fst = self.s1.get_min()
        snd = self.s2.get_min()
        return (fst if snd is None else snd) if fst is None or snd is None else min(fst, snd)

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()
