from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # First use case:
        # if endWord is not in wordList then return 0
        # However beginWord doesnt have to be part of wordList
        if endWord not in wordList:
            return 0
        
        # we build the adjacency list to store which replaced letter word matches to words in wordList, beginWord, or endWord
        nei = collections.defaultdict(list)
        # since we are gonna go through beginWord, just add it to wordList as well
        wordList.append(beginWord)
        # we are going to go thru every word in the wordList and each letter replacement to add to the Adjacency list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        # we perform BFS search on the words to see what is the shortest path we could take to traverse through the 
        # wordList
        visit = set(beginWord)
        q = collections.deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

        
        