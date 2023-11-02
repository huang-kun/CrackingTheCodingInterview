
from node import *

"""
使用额外集合储存链表值
"""

def remove_duplicates(node):
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


"""
如果题目要求不使用额外空间，根据提示使用双指针。
先写伪代码，明确思路
func remove_duplicates(node):
    for p in head..tail:
        for q in (p+1)..tail:
            if p == q:
                remove(q)
"""

def remove_duplicates_v2(node):
    if node is None:
        return
    
    base = node
    curr = base.next
    prev = base

    while base:
        while curr:
            if base.value == curr.value:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        base = base.next
        curr = base.next if base else None
        prev = base


def check(a, exp):
    n = list_to_nodes(a)
    remove_duplicates_v2(n)
    a1 = nodes_to_list(n)
    assert a1 == exp, f"remove duplicates failed: {a} -> {exp}, actual result: {a1}"


if __name__ == '__main__':
    check([3,5,7,2,5,3,6], [3,5,7,2,6])
    check([1,2,3,3,4,5,5], [1,2,3,4,5])
    check([2,2,2,1,1,1,2], [2,1])
