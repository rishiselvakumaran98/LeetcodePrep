class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Base conditions for invalid inputs
        if not head or left == right:
            return head
        
        # declare a dummy node to be used for reference for preLeft pointers
        dummyNode = ListNode()
        dummyNode.next = head

        preLeft = dummyNode

        # iterate all the way one node before the left marker
        for _ in range(left-1):
            preLeft = preLeft.next

        # Now start the reverse Node for currentNode
        currNode = preLeft.next
        prevNode = None

        for _ in range(right-left+1):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        preLeft.next.next = currNode
        preLeft.next = prevNode

        return dummyNode.next


        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def reverseBetween_not_working(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left:
            return head
        retPtr = head
        trailLeftPtr = None
        leftPtr = head
        rightPtr = head
        while rightPtr and rightPtr.val != right:
            if leftPtr.val != left:
                trailLeftPtr = leftPtr
                leftPtr = leftPtr.next
            
            rightPtr = rightPtr.next

        nextRightPtr = rightPtr.next
        rightPtr.next = None
        newLeftPtr, end = self.reverseList(leftPtr)
        trailLeftPtr.next = newLeftPtr
        end.next = nextRightPtr

        return retPtr



    def reverseList(self, head: Optional[ListNode]):
        prevPtr = None
        currPtr = head
        nextPtr = None

        while currPtr:
            nextPtr = currPtr.next
            currPtr.next = prevPtr
            prevPtr = currPtr
            currPtr = nextPtr
        
        lastPtr = head
        head = prevPtr
        return head, lastPtr