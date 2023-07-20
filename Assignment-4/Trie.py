"""
Keshav Shah

Trie

Implementation Complexity: O(n)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            # add chars to the trie that do not exist in the dict already
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            # move to the current character
            curr = curr.children[ch]

        curr.end = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        # curr.end will be True for words that do indeed exist in the Trie after insertion
        return curr.end

    def remove(self, word):
        curr = self.root
        for ch in word:
            curr = curr.children[ch]
        curr.end = False

def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("britain")
    trie.insert("art")
    trie.insert("brother")
    trie.insert("bro")

    print(trie.search("apple")) # True
    print(trie.search("britain")) # True
    print(trie.search("app")) # False
    print(trie.search("bro")) # True

    trie.remove("art")

    print(trie.search("art")) # False

main()
