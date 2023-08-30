from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # Helper method that calls and checks if the substring is valid
        # by checking if the length is met and if so add it to res
        # else for each of the 
        def dfs(substr: str, idx: int, path: str):
            # invalid condition
            print(path)
            if idx > 4:
                return
            if idx == 4 and not substr: # when the substr becomes empty
                res.append(path[:-1]) # we eliminate the dot at the end
                return
            
            for i in range(1, len(substr)+1):
                # we make sure either the inner port are 0 or they are number between 1 to 255 with no number starting at 0
                if substr[:i] == '0' or (substr[0] != '0' and 0 < int(substr[:i]) < 256):
                    dfs(substr[i:], idx+1, path+substr[:i]+".")

        dfs(s, 0, "")
        return res