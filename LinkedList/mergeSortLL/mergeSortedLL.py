# Definition for singly-linked list.
from typing import Optional


# The ListNode class represents a node in a linked list, with a value and a reference to the next
# node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iterative way --> Time: O(n), Space: O(1)
        ls1, ls2 = list1, list2
        prehead = ListNode(-1)
        prev = prehead

        while ls1 and ls2:
            if ls1.val <= ls2.val:
                prev.next = ls1
                ls1 = ls1.next
            else:
                prev.next = ls2
                ls2 = ls2.next
            prev = prev.next
        prev.next = ls1 if ls1 else ls2
        return prehead.next
    
    def mergeTwoListsRR(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive way --> Time: O(n), Space: O(n)

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        res = ListNode(-1)

        if list1.val <= list2.val:
            res.val = list1.val
            res.next = self.mergeTwoLists(list1.next, list2)
        else:
            res.val = list2.val
            res.next = self.mergeTwoLists(list1, list2.next)
        return res