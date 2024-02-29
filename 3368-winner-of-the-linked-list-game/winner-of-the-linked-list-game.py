# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        res, even = 0, head
        while even:
            res += 1 if even.val > even.next.val else -1
            even = even.next.next
        
        if res > 0: return 'Even'
        elif res < 0: return 'Odd'
        return 'Tie'