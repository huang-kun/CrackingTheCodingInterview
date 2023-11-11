from array import array
from multi_stack_in_one_base import FixSpacedMultiStackInOneBaseClass, testAllCases

class FixSpacedTripleInOne(FixSpacedMultiStackInOneBaseClass):
    """一个数组实现三栈合一"""

    def __init__(self, stackSize: int) -> None:
        self.stackCount = 3
        self.stackSize = stackSize
        self.counters = [0] * self.stackCount
        self.array = array('I', [0] * stackSize * self.stackCount)

    def getStackSize(self) -> int:
        """返回为每个栈分配的空间"""
        return self.stackSize

    def getStackCount(self) -> int:
        """返回所有栈的数量"""
        return self.stackCount

    def getItemCount(self, stackNum: int) -> int:
        """返回栈内的元素个数"""
        return self.counters[stackNum]
    
    def increaseItemCount(self, stackNum: int) -> None:
        """给栈内的元素个数加1"""
        self.counters[stackNum] += 1
    
    def decreaseItemCount(self, stackNum: int) -> None:
        """给栈内的元素个数减1"""
        self.counters[stackNum] -= 1
    
    def lastItemIndex(self, stackNum: int) -> int:
        """返回栈内的最后一个元素在数组中的下标位置。
        如果栈为空的话，会导致返回错误的位置。
        """
        baseIndex = stackNum * self.stackSize
        itemCount = self.counters[stackNum]
        return baseIndex + itemCount - 1


if __name__ == '__main__':
    testAllCases('triple_in_one.FixSpacedTripleInOne')