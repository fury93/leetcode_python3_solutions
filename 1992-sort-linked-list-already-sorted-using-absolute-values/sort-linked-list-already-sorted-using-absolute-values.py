# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            nxt = cur.next
            if nxt.val < 0:
                cur.next, nxt.next, head = nxt.next, head, nxt
            else:
                cur = nxt
        
        return head