'''
Keshav Shah

Question 3: Running Median
You will be given a stream of numbers, one by one. After each new number, return the median of the numbers so far.

Maintaining Two Heaps

Time Complexity: O(n log m) --> n elements to parse and insert with log m insertion
Space Complexity: O(n) --> n elements are being inserted

Process:
    - Create 2 heaps, the max heap will store the smaller half of the list and
      the min heap will store the larger half of the list
    - If the max heap is empty or the num < max in the max heap
      then add it to the max heap, otherwise add it to the min heap
      and then return the median

Time Spent: 38 minutes
'''

import heapq

def running_median():
    maxheap = []
    minheap = []

    while True:
        temp = input("Enter number: ")
        if temp == "done":
            break
        num = int(temp)

        # logic to find median

        # heapq is min heap, so we use negation to check
        # which heap we need to insert in
        if len(maxheap) == 0 or num < -maxheap[0]:
            heapq.heappush(maxheap, -num)
        else:
            heapq.heappush(minheap, num)

        # make sure the length of the heaps if within 1 of
        # each other at all times
        while len(maxheap) < len(minheap):
            # negated because we are using max heap
            heapq.heappush(maxheap, -heapq.heappop(minheap))
        while len(maxheap) > len(minheap) + 1:
            heapq.heappush(minheap, -heapq.heappop(maxheap))

        # return the median
        if len(maxheap) == len(minheap):
            median = (-maxheap[0] + minheap[0]) / 2.0
        else:
            median = -maxheap[0]

        print("The current median is: " + str(median))

running_median()

# Testing (All Cases Pass)
# Inputs:
# Input 1 --> Median 1
# Input 3 --> Median 2
# Input 4 --> Median 3
# Input 5 --> Median 3.5
# Input 6 --> Median 4

# Given Test Case
# Input: 1
# Output: 1
#
# Input: 1, 11
# Output: 6
#
# Input: 1, 11, 4
# Output: 4
#
# Input: 1, 11, 4, 15
# Output: 7.5
#
# Input: 1, 11, 4, 15, 12
# Output: 11

