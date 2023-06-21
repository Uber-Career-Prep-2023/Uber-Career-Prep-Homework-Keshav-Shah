'''
Keshav Shah

Question 9: Merge K Sorted Arrays
Given an array of k sorted arrays, merge the k arrays into a single sorted array.

Breadth-First Search

Time Complexity: O(k log n) (heap runs in log n time and there are k arrays)
Space Complexity: O(k*n) (n elements each of k arrays are being parsed)

Process:
    - Create a temp and result array where the temp array is the current
      status of the minheap
    - Keep appending the k arrays to the minheap and then pop the smallest element
      after all the arrays have been added to the minheap and add this popped element
      to the results array and output this array which will be the correct order

Time Spent: 35 minutes
'''

import heapq
def merge_k_sorted(k, arrays):
    temp = []
    output = []
    for arr in arrays:
        for val in arr:
            heapq.heappush(temp, val)
    while temp:
        output.append(heapq.heappop(temp))
    return output

def main():
    print(merge_k_sorted(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
    # Correctly outputs [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

    print(merge_k_sorted(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
    # Correctly outputs [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]

    print(merge_k_sorted(4, [[1], [2], [3], [4]]))
    # Correctly outputs [1, 2, 3, 4]

    print(merge_k_sorted(1, [[4, 3, 5, 2, 1]]))
    # Correctly outputs [1, 2, 3, 4, 5]

main()
