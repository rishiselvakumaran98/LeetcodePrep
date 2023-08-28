# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # construct a dfs method that recursively goes through the left and right nodes

        def validate(node, low, high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root, float('-inf'), float('inf'))
