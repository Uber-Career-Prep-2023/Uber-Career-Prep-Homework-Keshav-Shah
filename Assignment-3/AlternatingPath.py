'''
Keshav Shah

Question 8: Alternating Path
Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of
the shortest path from the origin to the destination in which the edges traversed alternate in color.
Return -1 if no such path exists.

Breadth-First Search

Time Complexity: O(n + m) (visit all the nodes and edges to check all possible paths)
Space Complexity: O(n + m) (paths stored in a dictionary)

Process:
    - Create dictionary where key is origin node and the value is a tuple
      consisting of the destination node and the color
    - Create a queue containing the current origin node, the length of the current path,
      and the color
    - If origin node matches the destination node a valid path has been found and return the length
    - If not, traverse through the neighbors of the origin node if the color is alternating

Time Spent: 39 minutes
'''

from collections import deque, defaultdict

def alternating_path(paths, origin, destination):
    # create adjacency list of all paths
    pathing = defaultdict(list)
    for start, end, color in paths:
        pathing[start].append((end, color))

    q = deque()
    # start at initial node with 0 length and no specified color
    q.append((origin, 0, None))
    while q:
        current_origin, length, color = q.popleft()
        # check if the current origin node is the destination
        if current_origin == destination:
            return length
        # check all neighbors of current origin node for possible pathing
        for next_loc, next_color in pathing[current_origin]:
            if next_color != color:
                q.append((next_loc, length + 1, next_color))

    return -1

def main():
    print(alternating_path([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"),
                            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"),
                            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")],
                           'A', 'E'))

    # Correct Output 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))

    print(alternating_path([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"),
                            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"),
                            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")],
                           'E', 'D'))

    # Correct Output -1 (only path is: E→C (red), C→B (red), B→D (blue))

    print(alternating_path([('A', 'B', "blue"), ('B', 'C', "red")], 'A', 'C'))

    # Correct Output 2 (path: A→B (red), B→C blue))

    print(alternating_path([('A', 'B', "blue")], 'A', 'B'))

    # Correct Output 1 (path: A→B (blue))

main()
