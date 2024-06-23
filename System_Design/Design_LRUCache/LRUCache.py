class DlinkedNode:
    def __init__(self, key=-1, val=-1, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # used to store the key to node
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_(node)
            self.add_(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_(self.cache[key])
        
        newNode = DlinkedNode(key, value)
        self.add_(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.capacity:
            remove_node = self.head.next
            self.remove_(remove_node)
            del self.cache[remove_node.key]
    
    def add_(self, node):
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node
    
    def remove_(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
