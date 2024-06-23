from collections import defaultdict

class DLinkedNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value=value
        self.prev=prev
        self.next=next

class DLinkedList: # LRU Cache List
    def __init__(self):
        self.left = DLinkedNode()
        self.right = DLinkedNode(prev=self.left)
        self.left.next = self.right
        self.hashMap = {}
    
    def length(self):
        return len(self.hashMap)
    
    def pushRight(self, val):
        node = DLinkedNode(val, self.right.prev, self.right)
        self.hashMap[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.hashMap:
            node = self.hashMap[val]
            prevNode, nextNode = node.prev, node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.hashMap.pop(val, None)
    
    def popLeft(self):
        if self.left.next == self.right:
            return None
        res = self.left.next.value
        self.pop(res)
        return res
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)


class LFUCache:
    # We implement this cache the same way as a LRU Cache
    # Except we keep track of the least frequently used item using a minHeap -> (count, key)

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        # LFU Cache
        self.lfuCnt = 1
        self.valMap = {} # Maps the key -> val
        self.countMap = defaultdict(int) # maps the key -> count
        self.listMap = defaultdict(DLinkedList) # maps count -> LinkedList of vals

    def addCount(self, key):
        """Helper method to increase counter value for the selected key"""
        # get the current counter value from the hashMap
        count = self.countMap[key] # returns 0 if the key is not found in the map
        # update countMap
        self.countMap[key] += 1
        # we need to update the self.listMap as well with new key value
        self.listMap[count].pop(key)
        self.listMap[count + 1].pushRight(key)

        # We need to add 1 for the least FU lists count
        if count == self.lfuCnt and self.listMap[count].length() == 0:
            self.lfuCnt += 1 # Create a new lfu

    def get(self, key: int) -> int:
        # We need to check if the key exists:
        if key not in self.valMap:
            return -1
        self.addCount(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        # If the capacity is 0 then we cannot add anything
        if self.capacity == 0:
            return -1
        
        # if we exceed the capacity we need to evict LFU List before adding this new node
        # if the key is already added then the eviction doesnt need to happen as it would only be an update operation
        if key in self.valMap:
            self.valMap[key]=value
            self.addCount(key)
        else:
            if len(self.valMap) == self.capacity:
                res = self.listMap[self.lfuCnt].popLeft() # remove the last 
                if res is not None:
                    self.valMap.pop(res)
                    self.countMap.pop(res)
            
            self.valMap[key] = value
            self.countMap[key] = 1
            self.listMap[1].pushRight(key)
            self.lfuCnt = min(self.lfuCnt, 1)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)