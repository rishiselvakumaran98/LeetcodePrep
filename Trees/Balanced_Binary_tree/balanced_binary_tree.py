# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # iterate through the tree and find its height
        # if the height of the abs(left tree - right tree) <= 1
        # and also if the left tree is balanced and right tree is balanced then return True
        def dfs(root):
            """
            The above function checks if a binary tree is balanced by recursively calculating the height
            of each subtree and checking if the difference in heights between the left and right
            subtrees is less than or equal to 1.
            
            :param root: The parameter "root" represents the root node of a binary tree
            :return: a boolean value indicating whether the binary tree rooted at `root` is balanced or
            not.
            """
            if not root:
                return (True, 0) 
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1
            height = 1 + max(left[1], right[1])

            return (balanced, height)

        return dfs(root)[0]
                