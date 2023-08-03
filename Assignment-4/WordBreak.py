'''
Keshav Shah

Question 6: Word Break
Given a string of characters without spaces and a dictionary of valid words, determine if it can be broken into
a list of valid words by adding spaces.

Dynamic Programming

Time Complexity: O(m*n) --> search the entire string and each word in the given dictionary
Space Complexity: O(n) --> dynamic programming array of booleans with the size of the input string

Process:
    - Create a dp array to store where in the string words are true
    - Iterate from the back of the list and check if certain substrings of the words are true
    - If they are, update the value of dp[i] to be the value of dp[i + length of the word]
    - If dp[i] is true that means that there are two valid words that are generated since the dp
      array is only true when it finds entire words

Time Spent: 38 minutes
'''

def word_break(input, words):
    dp = [False] * (len(input) + 1)
    dp[len(input)] = True

    # loop from the outermost to innermost letter
    for i in range(len(input) - 1, -1, -1):
        for w in words:
            w = w.lower()
            # check to see if current index is a feasible breakage point
            if (i + len(w)) <= len(input):
                # check if substring matches word in the dictionary
                if input[i : i + len(w)] == w:
                    # set current position to be true
                    dp[i] = dp[i + len(w)]
            # if dp[i] is true this means that the word up until dp[i] is already true
            # meaning that the word has been successfully partitioned
            if dp[i]:
                break

    return dp[0]

def main():

    words = ["Elf", "Go", "Golf", "Man", "Manatee",
             "Not", "Note", "Pig", "Quip", "Tee", "Teen"]

    print(word_break("mangolf", words))
    # Correct Output True

    print(word_break("manateenotelf", words))
    # Correct Output True

    print(word_break("quipig", words))
    # Correct Output False

    words2 = ["test", "run", "hello", "goodbye", "bye", "good"]

    print(word_break("goodbye", words2))
    # Correct Output True

    print(word_break("runtesthi", words2))
    # Correct Output False

    print(word_break("runthello", words2))
    # Correct Output False

main()
