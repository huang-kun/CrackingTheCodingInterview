
from listnode import *

"""
快慢双指针
"""
def find_last_kth(node, k):
    fast = node
    for _ in range(0, k):
        if fast is None:
            return None
        fast = fast.next
    
    slow = node
    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow


"""
递归，由于index和链表函数都是各自递归，会加剧时间复杂度。
"""
def backward_index(node):
    if node == None:
        return 0
    elif node.next == None:
        return 1
    else:
        return backward_index(node.next) + 1

def find_last_kth_recur(node, k):
    index = backward_index(node)
    if index < 1:
        return None
    elif index == k:
        return node
    else:
        return find_last_kth_recur(node.next, k)


"""
测试
"""
def check(a, k, exp):
    head = list_to_nodes(a)
    result = find_last_kth_recur(head, k)
    value = None
    if result is not None:
        value = result.val
    assert value == exp, f"find last kth failed: {a}, {k} -> {exp}, actual result: {value}"


if __name__ == '__main__':
    check([1,2,3], 2, 2)
    check([], 2, None)
    check([6,3,6,7], 4, 6)
    check([1], 1, 1)