class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        res, cur = [], root
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        