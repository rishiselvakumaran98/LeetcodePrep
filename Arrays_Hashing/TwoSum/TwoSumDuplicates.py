import bisect
from collections import defaultdict


class Solution:
    def twoSumDuplicates(self, nums, target: int):
        # Create a Dictionary to do indexMapping 
        indexMapping = defaultdict(list)
        for i in range(len(nums)):
            indexMapping[nums[i]].append(i)
        result = [0]*2
        # Now we search through the nums to find our target
        for i in range(len(nums)):
            currentNumber = nums[i]
            diff = target-nums[i]
            if(currentNumber == diff):
                if(len(indexMapping[currentNumber]) < 2):
                    continue
                result[0]=i
                indexList = indexMapping[currentNumber]
                indexOfI = bisect.bisect_left(indexList,i)
                result[1] = indexList[(indexOfI+1) % len(indexList)]
                break

            else: # default two sum problem 
                if len(indexMapping[diff]) == 0:
                    continue
                result[0]=i
                result[1] = indexMapping[diff][0]
                break

        return result


