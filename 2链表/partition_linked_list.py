
from listnode import *

def partition(head, x):
    """分割链表，leecode 86"""
    
    # 假设第一个大于等于x节点是f，那fp就是f的前驱节点，
    # 需要prev是为了方便其他小于x的节点插入到这里
    fp = None
    # 是否已经找到f
    found = False

    curr = head
    prev = None

    while curr:
        # 如果没有找到f，就先去找f
        if not found:
            # 找到了f，但如果f没有前驱节点，那fp就是null
            if curr.val >= x:
                found = True
                fp = prev
        
        # 找到f后继续遍历
        else:
            # 发现小于x的节点，需要往前换
            if curr.val < x:
                # 首先从链表里删除它
                prev.next = curr.next

                # 再把它往前换
                # 如果有fp，就插入到fp的后面
                if fp:
                    temp = fp.next
                    fp.next = curr
                    curr.next = temp

                    # 更新fp，这样后续插入就不会破坏链表节点的相对位置
                    fp = fp.next
                
                # 如果没有fp，就只能插入到头结点前面，再更换头结点
                else:
                    curr.next = head
                    head = curr
                    fp = head
                
                # 完成换位后，重新找回当前的位置，以便迭代能继续进行
                # 这里先把当前位置设为prev，因为循环最后会统一更新指针位置
                curr = prev
        
        # 更新指针位置，准备遍历下一个节点
        prev = curr
        curr = curr.next if curr else None
    
    return head


def check(a, x, exp):
    node1 = list_to_nodes(a)
    node2 = partition(node1, x)
    a2 = nodes_to_list(node2)
    assert a2 == exp, f"partition linked list failed: {a}, {x} -> {exp}, actual result: {a2}"


if __name__ == '__main__':
    check([1,4,3,2,5,2], 3, [1,2,2,4,3,5])
    check([2,1], 2, [1,2])
    check([4,3,2,5,2], 3, [2,2,4,3,5])
    
    # 目前金典的案例跟leetcode不同，当前按leetcode算的，所以先不考虑金典的
    # check([3,5,8,5,10,2,1], 5, [3,1,2,10,5,5,8])
