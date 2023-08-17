from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            other_num = target-nums[i]
            if other_num in visited:
                j = visited[other_num]
                return [i, j]
            visited[nums[i]] = i

        return [-1, -1]