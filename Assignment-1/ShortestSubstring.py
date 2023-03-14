'''
Keshav Shah

Question 5: ShortestSubstring
Given a string and a second string representing required characters, return the length of the
shortest substring containing all the required characters.

Two Pointers: Sorting Algorithm and Two Pointers: Variable Size Sliding Window

Time Complexity: O(n^2) as the sorting algorithm is O(nlogn) and the sliding window takes O(n^2)
Space Complexity: O(1) as there is no usage of any dynamic data structures

Process:
    - write a sort so that we can compare the input string with each substring by sorting the input and substring
    - if the sorted input string is in the sorted substring, then this would be a valid shortest substring
      so note down the length of this substring
    - return the length of the shortest such substring

Time Spent: 35 minutes
'''

# helper function to sort the strings in order to compare them
def sort_string(str):
    chars = list(str)
    sorted_chars = sorted(chars)
    sorted_string = "".join(sorted_chars)
    return sorted_string

def ShortestSubstring(str1, str2):

    # edge case in case one or both of the strings is empty in which case we return 0
    if len(str1) == 0 or len(str2) == 0:
        return 0

    sorted_component = sort_string(str2)
    min_length = float('inf')
    curr_length = float('inf')

    for i in range(len(str1)):
        for j in range(i+1, len(str1)+1):
            substr = str1[i:j]
            substr = sort_string(substr)
            if sorted_component in substr:
                curr_length = len(substr)
                if curr_length < min_length:
                    min_length = curr_length
    return min_length

def main():
    assert(ShortestSubstring("abracadabra", "abc") == 4)
    assert(ShortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx") == 10)
    assert(ShortestSubstring("dog", "god") == 3)

main() # all test cases pass
