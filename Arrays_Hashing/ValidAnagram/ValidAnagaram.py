import collections

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        There are figuratively a zillion ways to solve this problem
        but lets try to implement the more efficient and straight forward way
        and a one liner solution to solve this problem

        1. [Longer way] Using an array to store the 
        2. [One-liner] Using a Counter and frequency map to store the char and freq
        '''

        freqArray = [0]*26
        for char in s:
            index = ord(char.lower())-ord('a')
            freqArray[index] += 1
        for char in t:
            index = ord(char.lower())-ord('a')
            freqArray[index] -= 1
        
        for ele in freqArray:
            if ele != 0:
                return False
        return True
    
        # one-liner solution --> Warning only usable in python
    def isAnagramCounter(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

assert Solution().isAnagram("anagram", "nagaram")==True, "Assertion came out False"
assert Solution().isAnagram("rat", "car")==False, "Assertion came out True"
