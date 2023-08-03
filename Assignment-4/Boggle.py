'''
Keshav Shah

Question 2: Boggle
Given a Boggle board and a dictionary of valid words, return all valid words on the board.

Trie and Backtracking

Time Complexity: O(m*n) --> check all m letters in the board and n letters in the trie
Space Complexity: O(m*n) --> trie with n nodes and m pointers is made

Process:
    - Add all words to a trie
    - Use backtracking to check each words and all possible adjacent squares
      to see if there is another valid letter next to that word
    - If the word appears then add it to the output
    - Continue checking all possible adjacent squares for all possible squares in the board

Time Spent: 38 minutes
'''

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

def boggle(dictionary, board):
    trie = Trie()
    row, col = len(board), len(board[0])
    output = []
    visited = set()

    # insert valid words into trie
    for word in dictionary:
        word = word.lower()
        trie.insert(word)

    def backtrack(i, j, word):
        if i < 0 or j < 0 or i >= row or j >= col:
            return
        if (i, j) in visited:
            return

        word += board[i][j]

        if trie.search(word):
            output.append(word)

        visited.add((i, j))

        backtrack(i+1, j+1, word)
        backtrack(i+1, j, word)
        backtrack(i+1, j-1, word)
        backtrack(i, j+1, word)
        backtrack(i, j-1, word)
        backtrack(i-1, j-1, word)
        backtrack(i-1, j, word)
        backtrack(i-1, j+1, word)

        # remove the current letter as it might come up in different paths
        visited.remove((i, j))

    for r in range(row):
        for c in range(col):
            backtrack(r, c, "")

    return output

def main():
    dictionary = ["Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape",
             "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Rap",
             "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"]

    board = [
              ["a", "d", "e"],
              ["r", "c", "p"],
              ["l", "a", "y"]
    ]

    print(boggle(dictionary, board))
    # Correct Output: ['ace', 'ray', 'rap', 'cape', 'clay', 'clap',
    # 'pay', 'pace', 'lay', 'lace', 'lap', 'ace', 'ape', 'yap']

main()
