'''
Keshav Shah

Question 8: Coin Change
Given a list of coin denominations and a target sum, return the number of possible ways to make change for that sum.

Dynamic Programming

Time Complexity: O(n)
Space Complexity: O(n)

Process:
    - Create an array 1 larger than the desired target sum
    - Change the first index to 1 as there is 1 way to make 1
    - Then loop through the given array and then also do an inner loop from the current coin to the last element in dp
    - Then calculate how to add up to each number and return how many ways to add up to the sum

Time Spent: 35 minutes
'''

def coin_change(coins, target):

    dp = [0]*(target+1)
    # set 0th index to 1 since there is only one way to get to 0 coins
    dp[0] = 1

    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] += dp[i-coin]

    return dp[target]

def main():
    print(coin_change([2, 5, 10], 20)) # Correct Output 6
    print(coin_change([2, 5, 10], 15)) # Correct Output 3

main()
