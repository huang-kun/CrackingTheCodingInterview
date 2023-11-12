class StackOfPlates:

    def __init__(self, cap: int):
        self.stacks = [[]]
        self.cap = cap

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        elif len(self.stacks) == 0 or len(self.stacks[-1]) == self.cap:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)

    def pop(self) -> int:
        return self.popAt(-1)

    def popAt(self, index: int) -> int:
        if self.clearStackIfEmpty(index):
            return -1
        val = self.stacks[index].pop()
        self.clearStackIfEmpty(index)
        return val

    def clearStackIfEmpty(self, index: int) -> bool:
        if len(self.stacks) == 0 or index >= len(self.stacks):
            return True
        elif len(self.stacks[index]) == 0:
            del self.stacks[index]
            return True
        else:
            return False