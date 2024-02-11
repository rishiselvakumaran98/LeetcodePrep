from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we could use a partition based approach to use divide and conquer strategy to keep
        # dividing the linkedlist into 2 parts and then merging them tgt
        # we use a partition method to recursively divide the list

        return self.partition(0, len(lists)-1, lists)

    def partition(self, start, end, lists):
        if start == end:
            return lists[start]
        if start < end:
            q = (start+end)//2
            left = self.partition(start, q, lists)
            right = self.partition(q+1, end, lists)
            return self.mergeTwoLists(left, right)
        return None

    def mergeTwoLists(self, list1, list2):
        l1 = list1
        l2 = list2
        currentNode = ListNode()
        return_node = currentNode
        while l1 and l2:
            if l1.val < l2.val:
                currentNode.next = l1
                l1 = l1.next
            else:
                currentNode.next = l2
                l2 = l2.next
            currentNode = currentNode.next
        
        currentNode.next = l1 if l1 else l2
        return return_node.next




        
