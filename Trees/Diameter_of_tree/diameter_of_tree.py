# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        The function calculates the diameter of a binary tree.
        
        :param root: The root parameter is a reference to the root node of a binary tree
        :type root: Optional[TreeNode]
        """

        res = [0] # global variable as it would be accessible from inner recursive method

        def dfs(root):
            if not root:
                return -1 # To subtract from the 
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2+left+right) # Diameter = 2 + left + right

            return 1+ max(left, right) # Height running through the root of the tree
        dfs(root)
        return res[0]


        