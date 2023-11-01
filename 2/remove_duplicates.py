
from node import *

def remove_duplicates(node):
    # 使用额外集合储存链表值
    if node is None:
        return
    
    cache = set()
    cache.add(node.value)

    recurs_remove_duplicates(node.next, node, cache)

def recurs_remove_duplicates(node, prev, cache):
    if node is None:
        return
    
    deleted = False
    if node.value in cache:
        prev.next = node.next
        deleted = True
    else:
        cache.add(node.value)

    curr = node if not deleted else prev
    recurs_remove_duplicates(curr.next, curr, cache)


def remove_duplicates_v2(node):
    # 不使用额外空间，根据提示使用双指针
    pass


def check(a, exp):
    n = list_to_nodes(a)
    remove_duplicates(n)
    a1 = nodes_to_list(n)
    assert a1 == exp, f"remove duplicates failed: {a} -> {exp}, actual result: {a1}"


if __name__ == '__main__':
    check([3,5,7,2,5,3,6], [3,5,7,2,6])
    check([1,2,3,3,4,5,5], [1,2,3,4,5])
    check([2,2,2,1,1,1,2], [2,1])
