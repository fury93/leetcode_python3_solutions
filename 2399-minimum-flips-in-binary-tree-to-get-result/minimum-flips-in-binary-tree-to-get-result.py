# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        def dfs(node):
            if node.val == 0:
                return 1, 0
            if node.val == 1:
                return 0, 1

            if node.val == 5: # NOT
                t, f = dfs(node.left or node.right)
                return f, t

            lt, lf = dfs(node.left)
            rt, rf = dfs(node.right)
            
            if node.val == 2: # OR
                return min(lt + rt, lf + rt, lt + rf), lf + rf

            if node.val == 3: # AND
                return lt + rt, min(lt + rf, lf + rt, lf + rf)
            
            if node.val == 4: # XOR
                return min(lf + rt, lt + rf), min(lt + rt, lf + rf)
        
        t, f = dfs(root)
        return  t if result else f