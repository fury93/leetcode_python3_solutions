# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursion
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head
            
    # Iterative
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy #previous node before swapping
        while cur and cur.next and cur.next.next:
            first, second = cur.next, cur.next.next
            cur.next, first.next, second.next = second, second.next, first
            cur = cur.next.next
            
        return dummy.next
        