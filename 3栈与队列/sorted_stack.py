class SortedStack:

    def __init__(self):
        self.mainStack = []
        self.tempStack = []

    def push(self, val: int) -> None:
        while True:
            if len(self.mainStack) == 0 or self.mainStack[-1] >= val:
                self.mainStack.append(val)
                self.moveAllTempBack()
                break
            else:
                top = self.mainStack.pop()
                self.tempStack.append(top)

    def pop(self) -> None:
        return self.mainStack.pop() if len(self.mainStack) else -1

    def peek(self) -> int:
        return self.mainStack[-1] if len(self.mainStack) else -1

    def isEmpty(self) -> bool:
        return len(self.mainStack) == 0

    def moveAllTempBack(self) -> bool:
        while len(self.tempStack) > 0:
            top = self.tempStack.pop()
            self.mainStack.append(top)