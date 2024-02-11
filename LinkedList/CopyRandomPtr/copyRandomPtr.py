# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first create a deep copy of the current Random list into a dict
        # then use the dictionary to create another linkedlist with the references
        # above
        oldCopyDict = {None:None}
        currentPtr = head

        while currentPtr:
            nodePtr = Node(currentPtr.val)
            oldCopyDict[currentPtr] = nodePtr
            currentPtr = currentPtr.next
        
        currentPtr = head
        while currentPtr:
            copyPtr = oldCopyDict[currentPtr]
            copyPtr.next = oldCopyDict[currentPtr.next]
            copyPtr.random = oldCopyDict[currentPtr.random]
            currentPtr = currentPtr.next
        
        return oldCopyDict[head]
