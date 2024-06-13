class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self.heapify_up()
    
    def poll(self):
        item = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heapify_down()
        return item

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smallerIndex = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index):
                smallerIndex = self.get_right_child_index(index)
            
            if self.heap[index] < self.heap[smallerIndex]:
                break
            else:
                self.swap(index, smallerIndex)
            index = smallerIndex

    def get_parent_index(self, index):
        return (index - 1) // 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def parent(self, index):
        return self.heap[self.get_parent_index(index)]
    
    def get_left_child_index(self, index):
        return (index*2)+1
    
    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size
    
    def get_left_child(self, index):
        return self.heap[self.get_left_child_index(index)]
    
    def get_right_child_index(self, index):
        return (index*2)+2
    
    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size
    
    def get_right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def print_heap(self):
        print(self.heap)