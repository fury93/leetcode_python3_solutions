# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and root.left :
            res = self.upsideDownBinaryTree(root.left)
            root.left.right=root
            if root.right :
                root.left.left=root.right
            root.left =None
            root.right=None
            return res
        else:
            return root