'''
Keshav Shah

Question 5: Min Cost Stair Climbing
Given an array representing the costs per stair, what is the minimum possible toll you can pay to climb the staircase?

Dynamic Programming

Time Complexity: O(n)
Space Complexity: O(n)

Process:
    - Create array that counts to toll to go to each step
    - Loop from the third element onward and find the minimum cost between the available options
    - Return the value of the last or second last element of the array as this will be the cheapest toll cost

Time Spent: 32 minutes
'''

def min_cost_stair_climbing(arr):

    # edge case for small arrays
    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return min(arr[0], arr[1])

    cost = []
    for i in range(len(arr)):
        cost.append(0)

    cost[0] = arr[0]
    cost[1] = arr[1]

    for i in range(2, len(arr)):
        cost[i] = min(cost[i-1]+arr[i], cost[i-2]+arr[i])

    return min(cost[-2], cost[-1])


def main():
    print(min_cost_stair_climbing([11, 8, 3, 4, 9, 13, 10])) # Correct Output 25
    print(min_cost_stair_climbing([4, 1, 6, 3, 5, 8])) # Correct Output 9
    print(min_cost_stair_climbing([4, 7, 2, 1])) # Correct Output 6
    print(min_cost_stair_climbing([1, 1, 1, 1, 1])) # Correct Output 2

main()
