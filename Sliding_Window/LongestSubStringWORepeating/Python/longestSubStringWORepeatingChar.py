class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        longestSub = 0
        start = 0
        for i,c in enumerate(s):
            if c in lastSeen:
                start = max(start, lastSeen[c]+1)
            lastSeen[c] = i
            longestSub = max(longestSub, i-start+1)
        return longestSub