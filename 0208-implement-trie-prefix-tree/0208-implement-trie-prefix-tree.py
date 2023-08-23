class TrieNode:
    def __init__(self):
      self.children = {} # to hold children, using a hashmap
      self.endOfWord = False # to mark end of work

class Trie:
    def __init__(self):
        self.root = TrieNode() # initialize empty tree

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word: # iterate through each char and add as node to trie
          if c not in curr.children:
            curr.children[c] = TrieNode()
          curr = curr.children[c] # i.e. traverse / move down the tree
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
          if c not in curr.children:
            return False
          curr = curr.children[c]
        
        if curr.endOfWord:
          return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
          if c not in curr.children:
            return False
          curr = curr.children[c]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)