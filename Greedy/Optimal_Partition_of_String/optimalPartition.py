class Solution:
    def partitionString(self, s: str) -> int:
        lastIndexElement = {}
        for i,v in enumerate(s):
            lastIndexElement[v] = -1
        
        count, start = 1, 0
        for i,v in enumerate(s):
            if lastIndexElement[v] >= start:
                count += 1
                start = i
            lastIndexElement[v] = i
        return count