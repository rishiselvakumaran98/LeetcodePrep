class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
class Trie:

    def __init__(self):
        # we can create a rootNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        '''
        For each of the character if it doesnt exist as the TrieNode in the dictionary then add it 
        else set the current node as the children node
        '''
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord # true if we reached the end of the word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# word = "apple"
# prefix = "app"
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)