from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def findMaxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.findMaxDepth(root.left)
        right = self.findMaxDepth(root.right)
        return 1 + max(left, right)
    
    def preOrderTraversal(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        print(root.val, end="")
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def inOrderTraversal(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.inOrderTraversal(root.left)
        print(root.val, end="")
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.val, end="")

# Create a test tree
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Test the function with the sample tree
Solution().preOrderTraversal(root)
print()
    