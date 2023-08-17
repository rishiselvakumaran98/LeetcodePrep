# Definition for a binary tree node.
# The TreeNode class represents a node in a binary tree with a value, a left child node, and a right
# child node.
import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    Time: O(n)
    Space: O(n) --> queue will be largest at n/2, re
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We use BFS to do a level ordered search on the tree
        q= collections.deque()
        res = []
        q.append(root)
        # in the queue we add element to the right (append) and after done with the level
        # we popleft
        # as we remove the parent node we add the children node into the queue

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level: # we want to make sure the level are not empty
                res.append(level)
        return res