'''
Keshav Shah

Question 3: ZeroSumSubArrays
Given an array of integers, count the number of subarrays that sum to zero.

Two Pointers: Variable-Size (Growing/Shrinking) Sliding Window

Time Complexity: O(n^2) first we check if there are any 0 elements for the edge case which is O(n) complexity
                 Then we iterate through each subarray after a certain element which is a nested double for loop
                 which gives O(n^2) complexity since we are checking all possible subarrays
Space Complexity: O(1) since there are no dynamic data structures used or introduced

Process:
    - outer for loop iterates through each element
    - inner for loop checks all the subarrays from that element until the end of the array to see if there
      are any subarrays that add up to 0 as desired
    - return this number of subarrays

Time Spent: 35 minutes
'''

def ZeroSumSubArrays(arr):
    num_zero_subarrays = 0

    # edge case if the array is empty
    if len(arr) == 0:
        return None

    # edge case for the 0 element existing as a valid subarray is covered in this case
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if(sum(arr[i:j]) == 0):
                num_zero_subarrays += 1
    return num_zero_subarrays

def main():
    assert(ZeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7]) == 2)
    assert(ZeroSumSubArrays([1, 8, 7, 3, 11, 9]) == 0)
    assert(ZeroSumSubArrays([8, -5, 0, -2, 3, -4]) == 2)
    assert(ZeroSumSubArrays([0, 0, 0]) == 6)

main() # all test cases pass
