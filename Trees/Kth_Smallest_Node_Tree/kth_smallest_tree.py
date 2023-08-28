# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderTraversal(root):
            return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right) if root else []
        res = inOrderTraversal(root)
        return res[k-1]
    # solve the question the most brute force way
    def kthSmallestUnOptimized(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def preOrderTraversal(root):
            if not root:
                return
            
            res.append(root.val)
            preOrderTraversal(root.left)
            preOrderTraversal(root.right)
        
        preOrderTraversal(root)
        res.sort()
        return res[k-1]