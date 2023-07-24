'''
Keshav Shah

Question 4: Catalan Numbers
The Catalan numbers are a mathematical sequence of numbers. The nth Catalan number is defined as (2n)! / (n+1)!n!.
Given a non-negative integer n, return the Catalan numbers 0-n.

Dynamic Programming

Time Complexity: O(n^2) --> iterate nested for loop
Space Complexity: O(n) --> n Catalan numbers are generated

Process:
    - Catalan numbers can be represented by the following recurrence:
      Ci = Cj*C_(i-j-1)
    - We can use this recurrence to find n catalan numbers by storing previous values

Time Spent: 39 minutes
'''

def catalan_numbers(n):
    if n == 0 or n == 1:
        return [1]

    # create list of catalan numbers
    catalan = [0]*(n+1)

    # first two catalan number values
    catalan[0] = 1
    catalan[1] = 1

    # fill catalan list using the catalan recurrence relation
    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j]*catalan[i-j-1]

    return catalan

def main():
    print(catalan_numbers(1)) # Correct Output: 1
    print(catalan_numbers(5)) # Correct Output: 1, 1, 2, 5, 14, 42
    print(catalan_numbers(8)) # Correct Output: 1, 1, 2, 5, 14, 42, 132, 429, 1430

main()
