'''
Keshav Shah

Question 7: KAnagrams
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at
most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

Two Pointers: Simultaneous Iteration

Time Complexity: O(n) since n is the length of the string and we are iterating through the string and the characters
                 within the string in the set
Space Complexity: O(n) since the sets are dynamic objects that are being iterated through

Process:
    - create a map for each string and count the number of occurrences each letter has within each string
    - compare the number of occurrences of each letter through iteration, and if the number of occurrences
      for all the letters differs by more than k, then return False, else we return True

Time Spent: 38 minutes
'''

def KAnagrams(str1, str2, k):

    # edge case if the length of the strings is not equal then this property will never be satisfied
    if len(str1) != len(str2):
        return False

    map1 = {}
    map2 = {}
    charcount = 0

    for i in str1:
        if i not in map1:
            map1[i] = 1
        else:
            map1[i] += 1

    for i in str2:
        if i not in map2:
            map2[i] = 1
        else:
            map2[i] += 1

    for keys in map1.keys():
        if keys not in map2:
            charcount = charcount + map1[keys]
        else:
            if map1[keys] != map2[keys]:
                charcount = charcount + abs(map1[keys] - map2[keys])
        if charcount > k:
            return False

    return True

def main():
    assert(KAnagrams("apple", "peach", 1) == False)
    assert(KAnagrams("apple", "peach", 2) == True)
    assert(KAnagrams("cat", "dog", 3) == True)
    assert(KAnagrams("debit curd", "bad credit", 1) == True)
    assert(KAnagrams("baseball", "basketball", 2) == False)

main() # all test cases pass
