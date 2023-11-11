from array import array
from multi_stack_in_one_base import FixSpacedMultiStackInOneBaseClass, testAllCases

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

class FixSpacedTripleInOneOnly(FixSpacedMultiStackInOneBaseClass):
    """只用一个一维数组实现三栈合一"""

    def __init__(self, stackSize: int) -> None:
        stackCount = 3
        self.array = array('I', [stackSize, stackCount] + [0] * stackCount + [0] * stackSize * stackCount)

    def getStackSize(self) -> int:
        """返回为每个栈分配的空间"""
        return self.array[0]

    def getStackCount(self) -> int:
        """返回所有栈的数量"""
        return self.array[1]

    def getItemCount(self, stackNum: int) -> int:
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
        stackSize = self.getStackSize()
        stackCount = self.getStackCount()
        itemCount = self.getItemCount(stackNum)
        lastItemIndex = 2 + stackCount + stackNum * stackSize + itemCount - 1
        return lastItemIndex
    

if __name__ == '__main__':
    testAllCases('triple_in_one_1d.FixSpacedTripleInOneOnly')