# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node): # return (sum, nodes count)
            if not node: return (0, 0)
            l = dfs(node.left)
            r = dfs(node.right)
            sm = node.val + l[0] + r[0]
            cnt = 1 + l[1] + r[1]
            if (sm//cnt == node.val):
                nonlocal res
                res += 1
            return (sm, cnt)

        dfs(root)

        return res