# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we use a dfs method to traverse through the left and right nodes 
        # of the tree and increase count if the current node is greater than the max
        # else we set the count to 0
        count = 0
        def dfs(node, max_val):
            if not node:
                return 0

            count = 1 if node.val >= max_val else 0
            max_inPath = max(max_val, node.val)
            count += dfs(node.left, max_inPath)
            count += dfs(node.right, max_inPath)
            return count
        
        return dfs(root, root.val)

