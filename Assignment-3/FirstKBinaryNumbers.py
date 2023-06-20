'''
Keshav Shah

Question 5: FirstKBinaryNumbers
Given a number, k, return an array of the first k binary numbers, represented as strings.

Breadth-First Search

Time Complexity: O(k) (queue appends the values k times)
Space Complexity: O(k) (k strings are added to the list)

Process:
    - Create list that holds the binary values and add 0 to it (first binary number)
    - Create a queue where we will generate the next binary values given the pre-existing values
      so that every possible binary value will be correctly generated by adding a 0 or 1 to the end of each value
    - Add these newly generated values to the list until length k has been reached

Time Spent: 39 minutes
'''

from collections import deque

def first_k_binary_nums(k):

    # edge case
    if k <= 0:
        return []

    binary_nums = ['0']
    q = deque()
    q.append('1')

    while len(binary_nums) < k:
        val = q.popleft()
        if val:
            binary_nums.append(val)
        # generating next possible values that will be added to binary_nums
        q.append(val + '0')
        q.append(val + '1')

    return binary_nums

def main():
    print(first_k_binary_nums(5)) # Correct output ['0', '1', '10', '11', '100']

    print(first_k_binary_nums(10)) # Correct output ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']

    print(first_k_binary_nums(1)) # Correct output ['0']

main()
