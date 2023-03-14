'''
Keshav Shah

Question 4: BackspaceStringCompare
Given two strings representing series of keystrokes, determine whether the resulting text is the same.
Backspaces are represented by the '#' character so "x#" results in the empty string ("").

Two Pointers: Simultaneous Iteration and Stack

Time Complexity: O(n) as iterating through strings is constant time
Space Complexity: O(n) as using a dynamic object such as a stack is not constant

Process:
    - add each element of each of the strings to two individual stacks one for each string,
      and if the hashtag comes up, pop the element from the stack
    - if the stacks are equivalent after this iteration, then the strings are equal

Time Spent: 40 minutes
'''

def BackspaceStringCompare(str1, str2):

    # edge case in case both strings are empty in which case we return True
    if len(str1) == 0 and len(str2) == 0:
        return True

    # edge case in case one of the strings is empty in which case we return False
    if len(str1) == 0 or len(str2) == 0:
        return False

    stack1 = []
    stack2 = []

    for i in str1:
        if i == "#" and len(stack1) > 0:
            stack1.pop()
        else:
            stack1.append(i)

    for i in str2:
        if i == "#" and len(stack2) > 0:
            stack2.pop()
        else:
            stack2.append(i)

    return stack1 == stack2

def main():
    assert(BackspaceStringCompare("abcde", "abcde") == True)
    assert(BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep") == True)
    assert(BackspaceStringCompare("abcdef###xyz", "abcw#xyz") == True)
    assert(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###") == False)

main() # all test cases pass
