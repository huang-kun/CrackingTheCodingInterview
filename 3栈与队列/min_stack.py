class MinStack:

    def __init__(self):
        self.fullStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.fullStack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if len(self.fullStack) > 0:
            val = self.fullStack.pop()
            if len(self.minStack) > 0 and self.minStack[-1] == val:
                self.minStack.pop()

    def top(self) -> int:
        if len(self.fullStack) > 0:
            return self.fullStack[-1]
        else:
            return -1

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        else:
            return -1