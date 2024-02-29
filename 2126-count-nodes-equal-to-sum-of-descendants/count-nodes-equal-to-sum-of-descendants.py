# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node: return 0
            sm = dfs(node.left) + dfs(node.right)
            self.res += node.val == sm
            return sm + node.val
        dfs(root)
        return self.res 