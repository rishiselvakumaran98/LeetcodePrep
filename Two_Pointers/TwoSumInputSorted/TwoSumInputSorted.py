from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We use two pointers to iterate through the array, and we increment the left pointer if the sum
        is less than the target, and we decrement the right pointer if the sum is greater than the
        target
        
        :param numbers: List[int]
        :type numbers: List[int]
        :param target: The target number we are trying to find
        :type target: int
        :return: The indices of the two numbers such that they add up to a specific target.
        """
        # numbers array is already sorted   
        # We can use two pointers approach to solve this
        # However we need to skip duplications
        l = 0
        r = len(numbers)-1
        result = []
        while(l < r):
            sum_ = numbers[r] + numbers[l]
            if sum_ < target:
                l += 1
            if sum_ > target:
                r -= 1
            if sum_ == target:
                result += [l+1,r+1]
                break
        # Returning the result of the function.
        return result