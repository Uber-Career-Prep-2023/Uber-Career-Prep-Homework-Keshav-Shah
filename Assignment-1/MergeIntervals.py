'''
Keshav Shah

Question 8: MergeIntervals
Given a list of integer pairs representing the low and high end of an interval, inclusive,
return a list in which overlapping intervals are merged.

Sorting and Solving

Time Complexity: O(nlogn) since the complexity is determines by the sorting of the intervals which takes nlogn
Space Complexity: O(1) since there is no additional dynamic data stuctures used

Process:
    - first sort the intervals by the first element of each interval
    - compare the second element of an i-th interval with the first element of an i+1-st element
    - keep track of what intervals can be merged and return these intervals

Time Spent: 40 minutes (could not solve problem for test cases)
'''

def MergeIntervals(arr):

    # edge case if the array is initially empty
    if len(arr) == 0:
        return arr

    sorted_intervals = sorted(arr)
    final_intervals = []

    start = sorted_intervals[0]
    end = sorted_intervals[-1]

    for i, j in sorted_intervals[1:]:
        if i > end[0]:
            final_intervals.append((start, end))
            start = i
            end = j
        else:
            continue

    return final_intervals

def main():
    assert(MergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]) == [(4, 8), (1, 3), (9, 12)])
    assert(MergeIntervals( [(5, 8), (6, 10), (2, 4), (3, 6)]) == [(2, 10)])
    assert(MergeIntervals([(10, 12), (5, 6), (7, 9), (1, 3)]) == [(10, 12), (5, 6), (7, 9), (1, 3)])

main() # could not pass test cases
