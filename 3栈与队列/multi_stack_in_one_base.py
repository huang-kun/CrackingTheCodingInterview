from array import array
import importlib
import re

class MultiStackInOneBaseClass:
    """多栈合一的基类"""

    def __init__(self, stackSize: int) -> None:
        pass

    def push(self, stackNum: int, value: int) -> None:
        """入栈，如果栈已满，就忽略操作"""
        pass

    def pop(self, stackNum: int) -> int:
        """出栈，如果栈为空，返回-1"""
        pass

    def peek(self, stackNum: int) -> int:
        """查看栈顶元素，如果栈为空，返回-1"""
        pass

    def isEmpty(self, stackNum: int) -> bool:
        """查看栈是否为空"""
        pass
    
    def isFull(self, stackNum: int) -> bool:
        """查看栈是否已满"""
        pass
    
    def isOverflow(self, stackNum: int) -> bool:
        """查看栈是否溢出"""
        pass

    def getStackSize(self) -> int:
        """返回为每个栈分配的空间"""
        pass

    def getStackCount(self) -> int:
        """返回所有栈的数量"""
        pass

    def getItemCount(self, stackNum: int) -> int:
        """返回栈内的元素个数"""
        pass
    
    def increaseItemCount(self, stackNum: int) -> None:
        """给栈内的元素个数加1"""
        pass
    
    def decreaseItemCount(self, stackNum: int) -> None:
        """给栈内的元素个数减1"""
        pass
    
    def lastItemIndex(self, stackNum: int) -> int:
        """返回栈内的最后一个元素在数组中的下标位置。
        如果栈为空的话，会导致返回错误的位置。
        """
        pass


class FixSpacedMultiStackInOneBaseClass(MultiStackInOneBaseClass):
    """固定栈空间的多栈合一基类，默认实现了push, pop, peek, isEmpty"""

    def __init__(self, stackSize: int) -> None:
        self.array = array('I', [0] * stackSize * 3)

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
        return self.getItemCount(stackNum) == 0
    
    def isFull(self, stackNum: int) -> bool:
        """查看栈是否已满"""
        return self.getItemCount(stackNum) == self.getStackSize()
    
    def isOverflow(self, stackNum: int) -> bool:
        """查看栈是否溢出"""
        return self.getItemCount(stackNum) > self.getStackSize()


"""
测试
"""
def create_subclass_instance(subclass_name, **kwargs):
    # Import the module that contains the subclass
    module = importlib.import_module(subclass_name.split('.')[0])
    # Get the subclass class
    subclass_class = getattr(module, subclass_name.split('.')[-1])
    # Create a new instance of the subclass
    instance = subclass_class(**kwargs)
    # Return the instance
    return instance


def testAllCases(subclass_name: str):
    testLeetCodeCases(subclass_name)


LEETCODE_TEST = """
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
[null,null,null,1,-1,-1,true]

["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
[null,null,null,null,2,1,-1,-1]

["TripleInOne", "peek", "pop", "isEmpty", "push", "pop", "push", "push", "pop", "push", "push", "isEmpty", "pop", "peek", "push", "peek", "isEmpty", "peek", "pop", "push", "isEmpty", "pop", "peek", "peek", "pop", "peek", "isEmpty", "pop", "push", "isEmpty", "peek", "push", "peek", "isEmpty", "isEmpty", "isEmpty", "isEmpty", "peek", "push", "push", "peek", "isEmpty", "peek", "isEmpty", "push", "push", "push", "peek", "peek", "pop", "push", "push", "isEmpty", "peek", "pop", "push", "peek", "peek", "pop", "isEmpty", "pop", "peek", "peek", "push", "push"]
[[18], [1], [2], [1], [2, 40], [2], [0, 44], [1, 40], [0], [1, 54], [0, 42], [0], [1], [1], [0, 56], [2], [0], [2], [2], [1, 15], [1], [1], [0], [2], [0], [0], [1], [0], [0, 32], [0], [0], [0, 30], [2], [1], [1], [0], [0], [0], [0, 56], [1, 40], [2], [0], [0], [0], [2, 11], [0, 16], [0, 3], [2], [0], [2], [0, 39], [0, 63], [1], [2], [0], [2, 36], [1], [0], [2], [1], [0], [1], [2], [0, 8], [0, 38]]
[null,-1,-1,true,null,40,null,null,44,null,null,false,54,40,null,-1,false,-1,-1,null,false,15,56,-1,56,42,false,42,null,false,32,null,-1,false,false,false,false,30,null,null,-1,false,56,false,null,null,null,11,3,11,null,null,false,-1,63,null,40,39,36,false,39,40,-1,null,null]
"""

def testLeetCodeCases(subclass_name):

    def str_to_list(s, sep=","):
        return list(map(lambda x: x.strip(), s.split(sep)))
    
    def strip_brackets(s):
        has_start_bracket = s.startswith("[")
        has_end_bracket = s.endswith(']')
        if has_start_bracket and has_end_bracket:
            return s[1:-1]
        elif has_start_bracket:
            return s[1:]
        elif has_end_bracket:
            return s[:-1]
        else:
            return s
        
    def convert_type(s):
        if s.isdigit():
            return float(s) if '.' in s else int(s)
        else:
            return s

    components = LEETCODE_TEST.split('\n')
    commands, params, exps = (None, None, None)

    for string in components:
        # 执行测试
        if commands and params and exps:
            testLeetCodeCaseWithListForm(subclass_name, commands, params, exps)
            commands, params, exps = (None, None, None)

        if not string.startswith("["):
            continue
        
        # 解析期望结果
        elif commands and params:
            exps = str_to_list(strip_brackets(string))

        # 解析参数
        elif commands:
            subcomponents = str_to_list(strip_brackets(string), sep="], [")
            params = []
            for subcomponent in subcomponents:
                subitems = str_to_list(strip_brackets(subcomponent))
                subitems = list(map(lambda x: convert_type(x), subitems))
                params.append(subitems)

        # 解析指令
        elif string.startswith("[\"TripleInOne"):
            string = re.sub(r'"', '', strip_brackets(string))
            commands = str_to_list(string)

        else:
            continue


def testLeetCodeCaseWithListForm(subclass_name, commands, params, exps):
    obj = None
    count = len(commands)
    rets = []

    for i in range(count):
        command = commands[i]
        param = params[i]

        if command == "TripleInOne":
            # 创建实例对象
            obj = create_subclass_instance(subclass_name, stackSize=param[0])
            rets.append("null")
            continue

        # 获取对象方法
        func = getattr(obj, command)
        
        # 调用方法，把多个参数作为元祖传入，前面带星号（用来把元祖分解成位置参数）
        ret = func(*tuple(param))

        if ret == None:
            rets.append("null")
        elif type(ret) is bool:
            rets.append("true" if ret else "false")
        else:
            rets.append(str(ret))

        assert rets[i] == exps[i], f"test failed! f{command}({param}) -> {exps[i]}, actual result: {rets[i]}"

    assert rets == exps, f"test failed! expected results: {exps}, actual results: {rets}"

if __name__ == '__main__':
    pass