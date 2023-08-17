import collections


class Solution:
    def topKFrequent(self, nums, k):
        # Just use bucket sort to do this question
        # Setup a frequency map to map frequency of elements    
        # Setup buckets to hold the unique elements based on their element as index to hold their frequency
        # Then iterate through the buckets and to retrieve the elements from reverse order until k is met

        freqMap = {}
        maxFreq = -10**4
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
            maxFreq = max(maxFreq, freqMap[num])
        buckets = [[] for i in range(maxFreq+1)]
        
        for ele,freq in freqMap.items():
            buckets[freq].append(ele)
        print(buckets)
        count =0
        results = []
        for ele in buckets[::-1]:
            if count < k:
                results += ele
            count += 1
        return results
    
#  QuickSelect Method
    

