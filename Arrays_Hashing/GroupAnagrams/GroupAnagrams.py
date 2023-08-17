import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_groups = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            word_groups[sorted_word].append(word)
        return list(word_groups.values())