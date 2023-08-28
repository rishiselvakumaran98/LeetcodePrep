'''
In this problem we use a Trie to handle the specific word that we are traversing through to check the characters in them
'''
from typing import List
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
'''
For every single word we do dfs to check if the word occurrence happens there
Normal DFS would take len(words) * m*n*4^mn --> inefficient
Using Trie:
    We add all the words we need to search in a Trie and then use it as reference 
    we performing dfs in the board to see if we should continue searching a word
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # add the words to the Trie
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r,c) in visit or board[r][c] not in node.children):  # this word doesnt exist in the Trie hence we skip it
                return
            
            visit.add((r,c))
            node= node.children[board[r][c]] # we move on to the next 
            word += board[r][c]
            if node.isWord: # if we reached the end of the word in the trie then we add it to the results
                res.add(word)
            
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
        return list(res)
            # if the current node is endOfWord then we return True
