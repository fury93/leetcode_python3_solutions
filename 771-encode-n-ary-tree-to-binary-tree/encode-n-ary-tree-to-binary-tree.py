"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
# Approach 1: BFS (Breadth-First Search) Traversal
class Codec:
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None

        rootNode = TreeNode(root.val)
        queue = deque([(rootNode, root)])

        while queue:
            parent, curr = queue.popleft()
            prevBNode = None
            headBNode = None
            # traverse each child one by one
            for child in curr.children:
                newBNode = TreeNode(child.val)
                if prevBNode:
                    prevBNode.right = newBNode
                else:
                    headBNode = newBNode
                prevBNode = newBNode
                queue.append((newBNode, child))

            # use the first child in the left node of parent
            parent.left = headBNode

        return rootNode


    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        # should set the default value to [] rather than None,
        # otherwise it wont pass the test cases.
        rootNode = Node(data.val, [])

        queue = deque([(rootNode, data)])

        while queue:
            parent, curr = queue.popleft()

            firstChild = curr.left
            sibling = firstChild

            while sibling:
                # Note: the initial value of the children list should not be None, which is assumed by the online judge.
                newNode = Node(sibling.val, [])
                parent.children.append(newNode)
                queue.append((newNode, sibling))
                sibling = sibling.right

        return rootNode


# Approach 2: DFS (Depth-First Search) Traversal
class Codec2:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None

        rootNode = TreeNode(root.val)
        if len(root.children) > 0:
            firstChild = root.children[0]
            rootNode.left = self.encode(firstChild)

        # the parent for the rest of the children
        curr = rootNode.left

        # encode the rest of the children
        for i in range(1, len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right

        return rootNode


    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        rootNode = Node(data.val, [])

        curr = data.left
        while curr:
            rootNode.children.append(self.decode(curr))
            curr = curr.right

        return rootNode


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))