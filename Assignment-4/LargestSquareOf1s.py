'''
Keshav Shah

Question 7: Largest Square of 1s
Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.

Dynamic Programming

Time Complexity: O(r*c)
Space Complexity: O(r*c)

Process:
    - Create a DP array which is the same dimensions as the original array and set all the values to 0
    - Loop through the array and find a 1 and then check the left, top, and left-top boxes
    - If all of these are 1 then the box size can be increased so make the i, j element in the dp array to be 1
    - If the minimum of all the top, left, and top-left elements is 1 then the box size is now 2 etc.

Time Spent: 37 minutes
'''

def largest_square_of_1s(arr):

    # edge case for empty array
    if not arr:
        return 0

    dp = []
    size = 0

    for i in arr:
        dp.append([0]*len(arr[0]))

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                if dp[i][j] > size:
                    size = dp[i][j]

    return size

def main():
    m1 = [
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]
    ]

    print(largest_square_of_1s(m1)) # Correct Output 2

    m2 = [
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0]
    ]

    print(largest_square_of_1s(m2)) # Correct Output 3

    m3 = [
        [1, 0],
        [0, 0]
    ]

    print(largest_square_of_1s(m3)) # Correct Output 1

main()
