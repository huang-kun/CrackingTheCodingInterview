class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.rearrange()
        return self.outStack.pop() if len(self.outStack) else -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.rearrange()
        return self.outStack[-1] if len(self.outStack) else -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inStack) == 0 and len(self.outStack) == 0
    
    def rearrange(self) -> None:
        """
        move all elements from inStack to outStack when outStack is empty.
        """
        if len(self.outStack) > 0:
            return
        while len(self.inStack) > 0:
            val = self.inStack.pop()
            self.outStack.append(val)