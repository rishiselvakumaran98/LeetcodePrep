# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextPtr = None
        currentPtr = head
        prevPtr = None

        while currentPtr != None:
            nextPtr = currentPtr.next
            currentPtr.next = prevPtr
            prevPtr = currentPtr
            currentPtr = nextPtr

        head = prevPtr
        return head