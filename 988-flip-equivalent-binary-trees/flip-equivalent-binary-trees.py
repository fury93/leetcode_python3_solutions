# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        
        res = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        return res or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)