'''
Keshav Shah

Question 4: NumberOfIslands
Given a binary matrix in which 1s represent land and 0s represent water. Return the number of islands
(contiguous 1s surrounded by 0s or the edge of the matrix).

Depth-First Search

Time Complexity: O(n * m) (all locations in grid must be visited)
Space Complexity: O(1) (storing number of islands)

Process:
    - Visit grid locations until a 1 is reached
    - Find all neighboring 1s and mark them as visited to not double count
    - Increment the counter as an island has been found
    - Visit another unvisited grid location with a 1 and repeat process

Time Spent: 37 minutes
'''

def number_islands(board):

    rows, cols = len(board), len(board[0])
    num = 0

    def dfs(row, col):
        # if a non island square is reached return
        if row >= rows or row < 0 or col >= cols or col < 0:
            return
        if board[row][col] != 1:
            return
        # mark neighbor islands as visited
        board[row][col] = 'V'

        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

    # traversing the board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                dfs(r, c)
                num += 1

    return num


def main():
    board1 = [
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
             ]

    print(number_islands(board1)) # correctly outputs 3

    board2 = [
            [1, 0, 0],
            [0, 0, 0]
             ]

    print(number_islands(board2)) # correctly outputs 1

    board3 = [
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1]
             ]

    print(number_islands(board3))  # correctly outputs 13

    board4 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]

    print(number_islands(board4))  # correctly outputs 1

main()
