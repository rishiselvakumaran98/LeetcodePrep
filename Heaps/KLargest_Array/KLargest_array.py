from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k # reassign k so that it points exactly to the kth Smallest
        
        def quickSelect(l, r):
            pivot, p = nums[r], l # we choose the right most value as pivot, p pointer in the leftmost position 
            for i in range(l, r):
                if nums[i] <= pivot:
                    # we swap it with the left index which is p in this case
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # last part is that we need to swap the pivot or rightmost value with the p pointer value
            nums[p], nums[r] = nums[r], nums[p]

            if k < p: # if the k is less than p then we have to search the leftmost side of the array for quickselect
                return quickSelect(l, p-1)
            elif k > p:
                return quickSelect(p+1, r)
            else:
                return nums[p] # p is the kth largest
        return quickSelect(0, len(nums)-1)
