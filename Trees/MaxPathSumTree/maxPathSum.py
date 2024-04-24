from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            maxLeft = max(dfs(node.left), 0)
            maxRight = max(dfs(node.right), 0)

            res[0] = max(res[0], node.val + maxLeft + maxRight)

            return node.val + maxLeft + maxRight

        dfs(root)
        return res[0]    