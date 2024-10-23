# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(([root], 0, 0)) #nodes, sum, level
        levelSum = {}
        
        while queue:
            levelSize = len(queue)
            curLevelSum = 0
            for _ in range(levelSize):
                brotherNodes, brotherSum, level = queue.popleft()
                
                for node in brotherNodes:
                    #update node value
                    if level in [0,1]:
                        node.val = 0
                    else:
                        node.val = levelSum[level] - brotherSum
                    #process child nodes
                    childNodes = []
                    childSum = 0
                    if node.left:
                        childNodes.append(node.left)
                        childSum += node.left.val
                    if node.right:
                        childNodes.append(node.right)
                        childSum += node.right.val
                    curLevelSum +=childSum
                    queue.append((childNodes, childSum, level+1))
                    
                levelSum[level+1] = curLevelSum
        
        return root
            
            
        