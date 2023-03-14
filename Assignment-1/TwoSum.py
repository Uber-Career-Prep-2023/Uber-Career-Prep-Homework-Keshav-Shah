'''
Keshav Shah

Question 10: TwoSum
Given an array of integers and a target integer, k, return the number of pairs of integers in the array that sum to k.
In each pair, the two items must be distinct elements (come from different indices in the array).

Hashing: One Directional Running Computation

Time Complexity: O(n) since n is the length of the array
Space Complexity: O(n) since we are adding the unique elements from the original array to a dictionary

Process:
    - let each key in the created dictionary be the difference between k and each element in the array
    - if this element is equal to an existing key in the dictionary, we know that a possible sum has been found
    - if this difference is not found in the dictionary, add it and set its occurrence to be 1, otherwise
      add 1 to the existing occurrence of all key
    - if an existing sum is found increment count and then return this value

Time Spent: 45 minutes
'''

def TwoSum(arr, k):

    # edge case where the array has a length of less than 2 or is empty
    if len(arr) < 2:
        return None

    count = 0
    differences = {}

    for i in range(len(arr)):
        diff = k - arr[i]
        if arr[i] in differences:
            count = count + differences[arr[i]]
        if diff in differences:
            differences[diff] += 1
        else:
            differences[diff] = 1

    return count

def main():
    assert(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10) == 3)
    assert(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 9) == 4)
    assert(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6) == 5)
    assert(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1) == 0)

main() # all test cases pass
