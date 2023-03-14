'''
Keshav Shah

Question 2: ReverseVowels
Given a string, reverse the order of the vowels in the string.

Two Pointers: Forward/Backward

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) there is no additional usage of data structures beyond what is given

Process:
    - create two pointers and let the left pointer stop at the first vowel
      and let the right pointer stop at the last vowel
    - "swap" the vowels by creating a new string that puts the vowels in the desired location
    - return the new string

Time Spent: 35 minutes
'''

def ReverseVowels(str):

    # edge case where the string is empty
    if len(str) == 0:
        return None

    left = 0
    right = len(str) - 1
    vowels = ["a", "e", "i", "o", "u"]
    while left < right:
        if str[left].lower() in vowels:
            while str[right].lower() not in vowels:
                right = right - 1
            if left < right:
                str = str[0:left] + str[right] + str[left+1:right] + str[left] + str[right+1:len(str)]
        elif str[right].lower() in vowels:
            while str[left].lower() not in vowels:
                left = left + 1
            if left < right:
                str = str[0:left] + str[right] + str[left+1:right] + str[left] + str[right+1:len(str)]
        left = left + 1
        right = right - 1
    return str

def main():
    assert(ReverseVowels("Uber Career Prep") == "eber Ceraer PrUp")
    assert(ReverseVowels("xyz") == "xyz")
    assert(ReverseVowels("flamingo") == "flominga")

main() # all test cases pass
