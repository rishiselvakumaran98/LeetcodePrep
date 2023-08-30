# Definition for a binary tree node.
import collections
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # A binary tree is complete if there is no node to the right of the first null node
        # and no node at a greater level than first null node
        # we begin with root node and then return true if root is null
        # else we traverse thru and check if the node is null and we mark nullNodeFound = true
        # if we haven't visited the node and node != null we push the node.left and node.right
        # into the queue to traverse by each level
        if not root:
            return True
        nullNodeFound = False
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if not node:
                nullNodeFound = True
            else:
                if nullNodeFound:
                    return False
                # left or right can null which we use the if statement above to check
                q.append(node.left) 
                q.append(node.right)
        return True
