from listnode import *

"""
链表头结点代表数字最低位（个位）
e.g. 1->2->3, 321
"""
def sum_listnodes_v1(l1, l2):

    def to_num(node):
        num = 0
        n = 0
        curr = node
        while curr:
            num += (curr.val * pow(10, n))
            n += 1
            curr = curr.next
        return num

    def to_list(num):
        if num == 0:
            return ListNode(0)

        head = None
        prev = None
        while num > 0:
            val = num % 10
            num //= 10  # 易错点：python整除符号是“//”，使用“/”结果是小数，使用“int(num / 10)”会导致整型溢出
            curr = ListNode(val)
            if head is None:
                head = curr
            if prev:
                prev.next = curr
            prev = curr
        return head

    n1 = to_num(l1)
    n2 = to_num(l2)
    return to_list(n1 + n2)


"""
链表头结点代表数字最高位
e.g. 1->2->3, 123
"""
def sum_listnodes_v2(l1, l2):
     
    def len_of_list(node):
        size = 0
        curr = node
        while curr:
            size += 1
            curr = curr.next
        return size

    def to_num(node):
        num = 0
        n = len_of_list(node)
        curr = node
        while curr:
            num += (curr.val * pow(10, n-1))  # 易错点：链表长度与次方关系
            n -= 1
            curr = curr.next
        return num
    
    def to_list(num):
        head = None
        while num > 0:
            val = num % 10
            num //= 10
            curr = ListNode(val)
            curr.next = head
            head = curr
        return head
    
    n1 = to_num(l1)
    n2 = to_num(l2)
    return to_list(n1 + n2)


"""
测试
"""
def check(ver, a1, a2, exp):
    h1 = list_to_nodes(a1)
    h2 = list_to_nodes(a2)
    h3 = None
    if ver == 'v1':
        h3 = sum_listnodes_v1(h1, h2)
    elif ver == 'v2':
        h3 = sum_listnodes_v2(h1, h2)
    a3 = nodes_to_list(h3)
    assert a3 == exp, f"sum linked lists failed: {a1} + {a2} = {exp}, actual result: {a3}"

def check_v1(a1, a2, exp):
    check("v1", a1, a2, exp)

def check_v2(a1, a2, exp):
    check("v2", a1, a2, exp)

def check_algo_v1():
    check_v1([2,4,3], [5,6,4], [7,0,8])
    check_v1([1,2,3], [4,5,6], [5,7,9])
    check_v1([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [5,6,4], [6,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

def check_algo_v2():
    check_v2([2,4,3], [5,6,4], [8,0,7])
    check_v2([1,2,3], [4,5,6], [5,7,9])
    check_v2([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [5,6,4], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,5])


if __name__ == '__main__':
    check_algo_v1()
    check_algo_v2()