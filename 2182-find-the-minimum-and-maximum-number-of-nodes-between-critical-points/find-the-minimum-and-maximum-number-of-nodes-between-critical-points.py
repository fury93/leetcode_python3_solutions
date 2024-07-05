# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, cur, idx, i = head, head.next, [], 1
        while cur and cur.next:
            if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                idx.append(i)
            prev = cur
            cur = cur.next
            i += 1

        if len(idx) < 2:
            return [-1, -1]
        
        minDist = min(j - i for i, j in pairwise(idx))
        maxDist = idx[-1] - idx[0]

        return [minDist, maxDist]
