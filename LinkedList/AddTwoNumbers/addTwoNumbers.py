# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We iterate through l1 and l2:
        # we use two variables to keep track of sum
        # sum_ which contains l1.val + l2.val
        # carry_ which contains the remainder to carry to next sum sum_ // 10
        # at the end of loop, if carry_ still exists then add it to the next node
        current = ListNode()
        prehead = current
        list1 = l1
        list2 = l2
        
        carry_ = 0
        while list1 or list2:
            sum_ = 0
            if list1:
                sum_ += list1.val
                list1 = list1.next
            if list2:
                sum_ += list2.val
                list2=list2.next
            sum_ += carry_
            current.next = ListNode(sum_%10)
            carry_ = sum_//10
            current = current.next


        if carry_:
            current.next = ListNode(carry_)
        
        return prehead.next
        


    


