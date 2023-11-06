from listnode import *

"""
进阶题解：时间O(n)，空间O(1)
"""
def is_palindrome_linked_list(head):
    if head is None:
        return False
    elif head.next is None:
        return True

    # 快慢双指针找到中点 (slow, fast)
    fast = head
    slow = head
    prev = None
    half_count = 0
    while fast:
        fast = fast.next.next if fast.next else None
        prev = slow
        slow = slow.next
        half_count += 1

    # 反转链表后半部分 (prev, curr, next)
    curr = slow
    next = curr.next
    while curr:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next if next else None

    # 从头尾两端向中间遍历，判断回文 (p, q)
    p = head
    q = prev
    step = 0
    while step < half_count:
        if p.val != q.val:
            return False
        p = p.next
        q = q.next
        step += 1
    
    return True


def check(a, exp):
    n = list_to_nodes(a)
    assert is_palindrome_linked_list(n) == exp, f"palindrome linked list failed: {a} -> {exp}"


if __name__ == '__main__':
    check([1,2,2,1], True)
    check([1,2], False)
    check([1], True)
    check([1,2,3,2,1], True)
