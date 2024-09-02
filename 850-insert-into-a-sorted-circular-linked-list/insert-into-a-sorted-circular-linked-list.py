"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        cur = head.next
        while cur != head:
            # 1 => 2(insert) => 3 or 1 => 1 => 1(insert)
            if cur.val <= insertVal <= cur.next.val: break 
            # 2 => 3(insert) => 1 or 2 => 0 (insert) => 1
            if cur.val > cur.next.val and (insertVal > cur.val or insertVal < cur.next.val): break 
            cur = cur.next
        cur.next = Node(insertVal, cur.next)
        
        return head
