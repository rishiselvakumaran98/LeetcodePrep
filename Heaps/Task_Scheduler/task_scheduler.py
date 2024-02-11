from typing import List
from collections import Counter, deque
import heapq
class Solution:
    # Overall time -> O(n* log(26) * m) --> m is the idle time
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We can utilize a max_heap, which will allow us to continously 
        # to figure out which task is the most frequent one O(log(n))-->O(log(26))
        # We will also iterate over all the existing characters in the task -> O(n)
        # We will also use a Queue to keep track of the tasks to schedule
        # We take the most frequent element from the Max Heap and then decrement it since we are going to schedule it
        # we add the frequency of the char and its next placement time in the queue
        # the placement time will keep incrementing with give n time
        # when freq of char becomes 0 we dont add it back to the queue
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()] # we need to set freq neg for max heap
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q: # while one of these is not empty
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt: # if count is non-zero then append it to queue
                    q.append([cnt, time+n])
            if q and q[0][1] == time: # when the next char is in queue and it is time to process it
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                







