
class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_nodes(alist):
    head = None
    prev = None

    for elem in alist:
        node = ListNode()
        node.val = elem
        
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
        alist.append(curr.val)
        curr = curr.next
    
    return alist


def print_node(node):
    if node is None:
        return
    
    text = ""
    curr = node
    
    while curr:
        text += str(curr.val)
        if curr.next:
            text += "->"
        curr = curr.next
    
    print(text)