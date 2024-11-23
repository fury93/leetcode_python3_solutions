# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.total_sum = self.in_order_sum(root)
        return self.dfs(root)
        
        
    def in_order_sum(self, root):
        if not root:
            return 0 
        
        return self.in_order_sum(root.left) + root.val + self.in_order_sum(root.right)
    
    def dfs(self, root):
        if not root:
            return False
        
        if root.left:
            left_sum = self.in_order_sum(root.left) 
            if left_sum * 2 == self.total_sum:
                return True
        if root.right:
            right_sum = self.in_order_sum(root.right)
            if right_sum * 2 == self.total_sum:
                return True
        return self.dfs(root.left) or self.dfs(root.right)
        
class Solution2:
    def checkEqualTree(self, root):
        seen = []

        def sum_(node):
            if not node:
                return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total // 2.0 in seen