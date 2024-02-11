# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the lists and then add them from the rear end
        reversedL1 = self.reverseList(l1)
        reversedL2 = self.reverseList(l2)

        current = ListNode()
        return_node = current
        carry_ = 0
        while reversedL1 or reversedL2:
            sum_ = 0
            if reversedL1:
                sum_ += reversedL1.val
                reversedL1 = reversedL1.next
            if reversedL2:
                sum_ += reversedL2.val
                reversedL2 = reversedL2.next
            sum_ += carry_
            current.next = ListNode(sum_%10)
            carry_ = sum_//10
            current = current.next
        if carry_:
            current.next = ListNode(carry_)
        
        return self.reverseList(return_node.next)


        
    def reverseList(self, head):
        prev = nextPtr = None
        currentPtr = head
        while currentPtr:
            nextPtr = currentPtr.next
            currentPtr.next = prev
            prev = currentPtr
            currentPtr = nextPtr
        head = prev
        return head
