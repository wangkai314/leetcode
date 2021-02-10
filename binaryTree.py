class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def preorderTraversal(self, root:Node):
        if root is None:
            return []

        stack, output = [root,], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output

root = Node(1)
root.left = Node(2)
root.left.right = Node(3)

print(Solution.preorderTraversal(Solution, root))