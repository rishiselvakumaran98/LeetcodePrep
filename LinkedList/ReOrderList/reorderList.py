# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle node in the list
        # pass in the remaining elements from middleNode to be reversed
        # set the middleNode.next to None as we want it to be a separate reversed list
        # Now merge the two lists using mergeSortedLists
        middleNode = self.findMiddleNode(head)
        reversedNodes = self.reverseList(middleNode)
        middleNode.next = None
        return self.mergeList(head, reversedNodes)
    
    def findMiddleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prevPtr = None
        current = head
        nextPtr = None

        while current:
            nextPtr = current.next
            current.next = prevPtr
            prevPtr = current
            current = nextPtr
        
        head = prevPtr
        return head

    def mergeList(self, list1, list2):
        l1, l2 = list1, list2
        dummyNode = ListNode()
        ret_node = dummyNode
        alt_var = 1
        while l1 and l2:
            if alt_var%2 == 1:
                dummyNode.next = l1
                l1 = l1.next
            else:
                dummyNode.next = l2
                l2 = l2.next
            alt_var += 1
            dummyNode = dummyNode.next
        return ret_node.next
    

    