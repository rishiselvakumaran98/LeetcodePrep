from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Unoptimized Approach:
        # Time: O(n^2) for searching through in order array and constructing tree
        # Space: O(n)
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root
    
    def buildTreeOptimized(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # optimized Approach: O(n) using a Hashmap to store indexes of inorder elements
        inorderMap = { v:i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None
            
            root = TreeNode(postorder.pop())
            idx = inorderMap[root.val]
            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)
            return root
        return helper(0, len(postorder)-1)
    


