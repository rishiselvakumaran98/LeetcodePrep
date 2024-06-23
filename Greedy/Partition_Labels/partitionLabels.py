class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # First store the last Index of the letters into a HashMap
        # traverse through s and check if we can reach the max last index of one of the char
        # if so we can group that particular substring as a partition of s and move on to the other parts of the string

        lastIndexOfElement = {}
        for i,v in enumerate(s):
            lastIndexOfElement[v] = i
        # use variables end, size to check when we reach max last index of given char
        # and also check the size
        # store the size into res
        end, size = 0, 0
        res = []
        for i,v in enumerate(s):
            size += 1
            end = max(end, lastIndexOfElement[v])
            if i == end: # we found a partition end
                res.append(size)
                size = 0
        return res
