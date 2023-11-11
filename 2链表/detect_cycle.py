from listnode import *

def detect_cycle(head):
    slow = head
    fast = head

    # 快慢指针确定链表是否存在环
    while slow and fast:
        slow = slow.next
        fast = fast.next.next if fast.next else None
        if slow is fast:
            break
    
    # 如果存在环，再用双指针同步寻找环入口
    if slow and slow is fast:        
        p = head
        q = slow
        while p and q:
            if p is q:
                return p
            p = p.next
            q = q.next
        
    return None