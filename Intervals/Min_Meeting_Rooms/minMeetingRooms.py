import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        

        # There are two ways to solving this problem:
        # 1. Using a heap
        # 2. Using two sorted arrays (Chronological Ordering)

        # We can use a heap to keep track of the earliest end time
        if not intervals:
            return 0
        occupied_rooms = []
        # Sort the intervals based on the start time in ascending order
        intervals.sort(key=lambda x:x[0])

        # Add the first end time to the minHeap
        occupied_rooms.append(intervals[0][1])
        for interval in intervals[1:]:
            # If the room we have in the minHeap has lesser end time then the current start time 
            # we can free up a room as it can be occupied by the next person
            if occupied_rooms[0] <= interval[0]:
                heapq.heappop(occupied_rooms)
            
            # We can add the next interval to the occupied rooms
            heapq.heappush(occupied_rooms, interval[1])
        return len(occupied_rooms)

    def minMeetingRooms_Chrono_Ordering(self, intervals: List[List[int]]) -> int:
        # We can keep two sorted arrays to track the earliest start times in ascending order
        # we can keep a sorted array to track the earliest end time in ascending order
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        s,e = 0,0
        count = 0
        res = 0

        while s < len(intervals):
            if start[s]  < end[e]:
                # we need additional rooms and so we add one
                s += 1
                count += 1
                res = max(res, count)
            else:
                e += 1
                count -= 1
        return res