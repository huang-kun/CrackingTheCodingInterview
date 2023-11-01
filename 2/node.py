
class Node:
    
    def __init__(self):
        self.value = None
        self.next = None


def list_to_nodes(alist):
    head = None
    prev = None

    for elem in alist:
        node = Node()
        node.value = elem
        
        if head is None:
            head = node
        
        if prev is not None:
            prev.next = node

        prev = node

    return head


def nodes_to_list(node):
    if node is None:
        return []
    
    alist = []
    curr = node
    
    while curr:
        alist.append(curr.value)
        curr = curr.next
    
    return alist


def print_node(node):
    if node is None:
        return
    
    text = ""
    curr = node
    
    while curr:
        text += str(curr.value)
        if curr.next:
            text += "->"
        curr = curr.next
    
    print(text)