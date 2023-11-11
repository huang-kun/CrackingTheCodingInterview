from listnode import *

def get_intersection_node(headA, headB):
    # 分别计算链表长度
    def getLen(node):
        size = 0
        curr = node
        while curr:
            size += 1
            curr = curr.next
        return size
    
    lenA = getLen(headA)
    lenB = getLen(headB)

    # 长的先行
    a = headA
    b = headB

    diff = lenA - lenB
    step = diff if diff >= 0 else -diff
    
    while step > 0:
        if diff > 0:
            a = a.next if a else None
        else:
            b = b.next if b else None
        step -= 1
    
    # 寻找交点
    while a and b:
        if a is b:
            return a
        a = a.next
        b = b.next
    
    return None


def check(listA, listB, skipA, skipB, exp):
    headA = list_to_nodes(listA[:skipA])
    headB = list_to_nodes(listB[:skipB])

    tailA = find_tail(headA)
    tailB = find_tail(headB)

    restA = list_to_nodes(listA[skipA:])

    tailA.next = restA
    tailB.next = restA

    headC = get_intersection_node(headA, headB)
    listC = nodes_to_list(headC)

    err_msg = f"get intersection node failed: {listA}, {listB}, skipA={skipA}, skipB={skipB}, exp={exp}, actual result: {listC}"
    assert listC == exp, err_msg
    while skipA > 0:
        headA = headA.next
        skipA -= 1
    while skipB > 0:
        headB = headB.next
        skipB -= 1
    assert headA is headC, err_msg
    assert headB is headC, err_msg


def find_tail(node):
    curr = node
    while curr.next:
        curr = curr.next
    return curr


if __name__ == '__main__':
    check(listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3, exp = [8,4,5])
    check(listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1, exp = [2,4])
    check(listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2, exp = [])