'''
Keshav Shah

Question 6: MissingInteger
Given an integer n and a sorted array of integers of size n-1
which contains all but one of the integers in the range 1-n, find the missing integer.

Brute Force Iteration

Time Complexity: O(n) since n is the length of the array (is it possible to complete in O(log n)?
Space Complexity: O(1) since the size of the array does not change

Process:
    - consider edge cases where the array is empty and has only one element and simply return n for these cases
    - for all other cases, compare the iterating variable's value with the value in the array and if they do not match
      return the value of the iterating variable since this is what the missing integer is going to be

Time Spent: 20 minutes
'''

def MissingInteger(n, arr):

    # edge case where array is empty or if the array has one element
    if len(arr) == 0 or len(arr) == 1:
        return n

    # n input seems to be unnecessary
    for i in range(len(arr)):
        if i+1 != arr[i]:
            return i+1


def main():
    assert(MissingInteger(7, [1, 2, 3, 4, 6, 7]) == 5)
    assert(MissingInteger(2, [1]) == 2)
    assert(MissingInteger(12, [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]) == 9)

main() # all test cases pass
