'''
Keshav Shah

Question 9: DedupArray
Given a sorted array of non-negative integers, modify the array by removing duplicates so each element appears once.
If arrays are static (aka, not dynamic/resizable) in your language of choice, the remaining elements should appear in
the left-hand side of the array and the extra space in the right-hand side should be padded with -1s.

Array Iteration and Sets

Time Complexity: O(n) since n is the length of the array
Space Complexity: O(n) since we are adding the unique elements from the original array to a set

Process:
    - iterate through the inputted array and add all the elements of the array to a set
    - put all the elements of the set into an array and return this as there are no duplicates in a set

Time Spent: 25 minutes
'''

def DedupArray(arr):

    # edge case if the array is empty return the empty array
    if len(arr) == 0:
        return arr

    uniquevals = set()
    uniquearr = []

    for i in range(len(arr)):
        uniquevals.add(arr[i])

    for j in uniquevals:
        uniquearr.append(j)

    return uniquearr

def main():
    assert(DedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 2, 3, 4])
    assert(DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]) == [0, 1, 4, 5, 8, 9, 10, 11, 15])
    assert(DedupArray([1, 3, 4, 8, 10, 12]) == [1, 3, 4, 8, 10, 12])

main() # all test cases pass
