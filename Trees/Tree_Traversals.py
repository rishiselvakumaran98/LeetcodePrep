from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return str(self.val)

def preOrderTraversalRecursion(root):
     if not root:
         return ""
     
     print(root.val, end=" ")
     preOrderTraversalRecursion(root.left)
     preOrderTraversalRecursion(root.right)

def preOrderTraversalIterative(root):
    curr, stack = root, []
    res = []

    while curr or stack:
        if curr:
            res.append(curr.val)
            stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return res
        
def inOrderTraversalRecursion(root):
    if not root:
        return ""
    inOrderTraversalRecursion(root.left)
    print(root.val, end = " ")
    inOrderTraversalRecursion(root.right)

def inOrderTraversalIterative(root):
    curr, stack = root, []
    res = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr)
        curr = curr.right
    
    return res


def postOrderTraversalRecursion(root, returnArr):
    if not root:
        return 
    postOrderTraversalRecursion(root.left, returnArr)
    postOrderTraversalRecursion(root.right, returnArr)
    # print(root.val, end=" ")
    returnArr.append(root)

def postOrderTraversalIterative(root):
    stack = [(root, False)]
    res= []

    while stack:
        (curr, v) = stack.pop()
        if curr:
            if v:
                res.append(curr.val)
            else:
                stack.append((curr, True))
                stack.append((curr.right, False))
                stack.append((curr.left, False))

    return res



    


def isSymmetric(root):
    if not root:
        return True
    
    def compare(left, right):
        if not left and not right:
            return True
        elif not left or not right or left.val != right.val:
            return False
        else:
            return compare(left.left, right.right) and compare(left.right, right.left)
        
    return compare(root.left, root.right)


def isSymmetricLoop(root):
    if not root:
        return True
    
    q = deque()
    q.append((root.left, root.right))

    while q:
        (left, right) = q.popleft()
        if not left and not right:
            continue
        if not left or not right or left.val != right.val:
            return False
        q.append((left.left, right.right))
        q.append((left.right, right.left))
    return True

# Driver program to test above function
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
# preOrderTraversalRecursion(root)
# print()
print(postOrderTraversalIterative(root))
# print()
# returnArr = []
# postOrderTraversalRecursion(root, returnArr)
# print(returnArr)