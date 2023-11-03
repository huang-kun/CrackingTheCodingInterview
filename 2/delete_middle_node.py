
from node import *

"""
迭代遍历
"""
def delete_middle_node(node):
    curr = node
    prev = None

    while curr:
        if curr.next:
            curr.value = curr.next.value
        elif prev:
            prev.next = None
        prev = curr
        curr = curr.next


"""
递归
"""
def delete_middle_node_v2(node):
    if node is None:
        return
    delete_middle_node_recur(node, None)

def delete_middle_node_recur(node, prev):
    if node is None:
        return
    if node.next:
        node.value = node.next.value
    elif prev:
        prev.next = None
    delete_middle_node_recur(node.next, node)


"""
测试
"""
def check(a, i, exp):
    node = list_to_nodes(a)

    curr = node
    for index in range(len(a)):
        if index == i or curr == None:
            break
        curr = curr.next

    delete_middle_node(curr)
    a1 = nodes_to_list(curr)
    a2 = a[:i] + a1
    assert a2 == exp, f"delete middle node failed: {a}, {i} -> {exp}, actual result: {a2}"


if __name__ == '__main__':
    # 测试示例中不能要求删除最后一个节点，因为无法获取前置节点
    check([1,3,4,2,4], 1, [1,4,2,4])
    check([8,5,4,9,3], 3, [8,5,4,3])
    check([1,1,2,3], 0, [1,2,3])
    check([1,2], 0, [2])
