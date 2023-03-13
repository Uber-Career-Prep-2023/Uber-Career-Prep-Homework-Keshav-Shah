'''
Keshav Shah

Question 1: MaxMeanSubArray
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Two Pointers: Fixed Size Sliding Window

Time Complexity: O(n): n is the size of the array
Space Complexity: O(1): array is statis not dynamic

Process:
    - create sliding window
    - iterate through all sliding windows and check the window with the max mean
    - return window with the max mean

Time Spent: 30 minutes
'''

def MaxMeanSubArray(arr, k):
    max_mean = -1
    left = 0
    right = k

    # edge cases (array is empty or if k is greater than the length of the array
    if len(arr) < k or not arr:
        return None

    while right < len(arr) + 1:
        curr_mean = sum(arr[left:right])/k
        max_mean = max(max_mean, curr_mean)
        left += 1
        right += 1
    # print(max_mean)
    return max_mean

def main():
    assert(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 2) == 4.5)
    assert(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 3) == 3)
    assert(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3) == 1)
    assert(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5) == 1)

main() # all test cases pass
