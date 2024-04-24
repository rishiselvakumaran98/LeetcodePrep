from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we use a res variable to keep track of the max diff
        # between the first node in the level vs the last node

        # we use a BFS approach to traverse level by level in the tree
        # to find which is the max width
        # we could setup three variables in q queue:
        # (node, num, level)

        res = 0
        q = deque([(root, 1, 0)])
        prevNum, prevLevel = 1, 0
        while q:
            node, num, level = q.popleft()

            if level > prevLevel:
                prevLevel = level
                prevNum = num

            # we update the result with the maximum width at this current level
            res = max(res, num - prevNum+1)

            if node.left:
                q.append((node.left, 2*num, level+1))
            if node.right:
                q.append((node.right, 2*num+1, level+1))
        return res
