# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        The function `isSameTree` checks if two binary trees `p` and `q` are identical by recursively
        comparing their values and the values of their left and right subtrees.
        
        :param p: The parameter `p` is of type `Optional[TreeNode]`, which means it can either be a
        `TreeNode` object or `None`. It represents the root of the first binary tree
        :type p: Optional[TreeNode]
        :param q: The parameter `q` is of type `Optional[TreeNode]`, which means it can either be a
        `TreeNode` object or `None`. It represents the root of the second binary tree
        :type q: Optional[TreeNode]
        :return: a boolean value, indicating whether the two input trees are the same or not.
        """
        '''
        if both p and q are None, meaning they are empty trees, hence they are same
        '''
        if not p and not q:
            return True
        '''
        If one of them is None and the other is not, it means the trees are not the same
        '''
        if not p or not q:
            return False
        '''
        if the values of their root nodes (p.val and q.val) are not the same, return False
        '''
        if p.val != q.val:
            return False
        '''
        if the values of the root nodes are the same, the function calls itself recursively for the left subtrees and the right subtrees of p and q
        '''
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)