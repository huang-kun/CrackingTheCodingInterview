from array import array

"""
用一个数组实现三个栈，这里的思路是把数组下标划分为不同的功能区域：
stackCount = 3
- index [0]: 保存stackSize（指定每个栈的长度）
- index [1]: 保存栈的数量，题目中要求是3个栈，所以是3
- index [2, 2 + stackCount - 1]: 保存每个栈内的元素个数，初始为0
- index [2 + stackCount, ~]: 保存实际栈

举例：
实现3个栈，每个栈最多2个元素: [2] + [3] + [0,0,0] + [0,0] + [0,0] + [0,0] = [2,3,0,0,0,0,0,0,0,0,0]
给栈0添加5，栈1添加6和7: [2,3,1,2,0,5,0,6,7,0,0]

实现2个栈，每个栈最多1个元素: [1] + [2] + [0,0] + [0] + [0] = [1,2,0,0,0,0]
给栈0添加3，栈1添加4: [1,2,1,1,3,4]
"""

class TripleInOne:

    def __init__(self, stackSize: int) -> None:
        stackCount = 3
        self.array = array('I', [stackSize, stackCount] + [0] * stackCount + [0] * stackSize * stackCount)

    def push(self, stackNum: int, value: int) -> None:
        """入栈，如果栈已满，就忽略操作"""
        if self.isFull(stackNum):
            return None
        pushIndex = self.lastItemIndex(stackNum) + 1
        self.array[pushIndex] = value
        self.increaseItemCount(stackNum)

    def pop(self, stackNum: int) -> int:
        """出栈，如果栈为空，返回-1"""
        if self.isEmpty(stackNum):
            return -1
        lastIndex = self.lastItemIndex(stackNum)
        value = self.array[lastIndex]
        self.decreaseItemCount(stackNum)
        return value

    def peek(self, stackNum: int) -> int:
        """查看栈顶元素，如果栈为空，返回-1"""
        if self.isEmpty(stackNum):
            return -1
        lastIndex = self.lastItemIndex(stackNum)
        return self.array[lastIndex]

    def isEmpty(self, stackNum: int) -> bool:
        """查看栈是否为空"""
        return self.itemCount(stackNum) == 0
    
    def isFull(self, stackNum: int) -> bool:
        """查看栈是否已满"""
        return self.itemCount(stackNum) == self.stackSize()
    
    def isOverflow(self, stackNum: int) -> bool:
        """查看栈是否溢出"""
        return self.itemCount(stackNum) > self.stackSize()

    def stackSize(self) -> int:
        """返回为每个栈分配的空间"""
        return self.array[0]

    def stackCount(self) -> int:
        """返回所有栈的数量"""
        return self.array[1]

    def itemCount(self, stackNum: int) -> int:
        """返回栈内的元素个数"""
        countIndex = 2 + stackNum
        itemCount = self.array[countIndex]
        return itemCount
    
    def increaseItemCount(self, stackNum: int) -> None:
        """给栈内的元素个数加1"""
        countIndex = 2 + stackNum
        self.array[countIndex] += 1
    
    def decreaseItemCount(self, stackNum: int) -> None:
        """给栈内的元素个数减1"""
        countIndex = 2 + stackNum
        self.array[countIndex] -= 1
    
    def lastItemIndex(self, stackNum: int) -> int:
        """返回栈内的最后一个元素在数组中的下标位置。
        如果栈为空的话，会导致返回错误的位置。
        """
        stackSize = self.stackSize()
        stackCount = self.stackCount()
        itemCount = self.itemCount(stackNum)
        lastItemIndex = 2 + stackCount + stackNum * stackSize + itemCount - 1
        return lastItemIndex


"""
测试
"""
def testCase1():
    obj = TripleInOne(1)
    assert obj.stackSize() == 1
    
    obj.push(0,1)
    assert obj.itemCount(0) == 1
    assert obj.peek(0) == 1
    
    obj.push(0,2)
    assert obj.itemCount(0) == 1
    assert obj.peek(0) == 1

    param_1 = obj.pop(0)
    assert param_1 == 1

    param_2 = obj.pop(0)
    assert param_2 == -1

    param_3 = obj.pop(0)
    assert param_3 == -1

    param_4 = obj.isEmpty(0)
    assert param_4 == True


def testCase2():
    obj = TripleInOne(2)
    assert obj.stackSize() == 2

    obj.push(0,1)
    assert obj.itemCount(0) == 1
    assert obj.peek(0) == 1

    obj.push(0,2)
    assert obj.itemCount(0) == 2
    assert obj.peek(0) == 2

    obj.push(0,3)
    assert obj.itemCount(0) == 2
    assert obj.peek(0) == 2
    
    param_1 = obj.pop(0)
    assert param_1 == 2

    param_2 = obj.pop(0)
    assert param_2 == 1
    
    param_3 = obj.pop(0)
    assert param_3 == -1
    
    param_4 = obj.peek(0)
    assert param_3 == -1


if __name__ == '__main__':
    testCase1()
    testCase2()