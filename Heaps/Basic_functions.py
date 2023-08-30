import heapq


def main():
    # turning a list into a heap:

    a = [3, 5, 1, 2, 6, 8, 7] # unsorted list
    # need to heapify in order to use the properties of heap on the list
    heapq.heapify(a) # modifies list in-place --> a = [1, 2, 3, 5, 6, 8, 7]
    # To pop the smallest element:
    smallest_ele = heapq.heappop(a) # 1
    # a becomes a =  [2, 5, 3, 7, 6, 8] 

    # pushing ele while maintaining heap property:
    heapq.heappush(a, 4)

    # retrieving a list of n smallest elements:
    smallest_3 = heapq.nsmallest(3, a)