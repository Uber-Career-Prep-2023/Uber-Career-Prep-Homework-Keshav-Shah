"""
Keshav Shah

Question 11: Vacation Destinations
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each
other with corresponding travel times in hours, return the number of destinations within k hours of the origin.
Assume that having a stopover in a city adds an hour of travel time.

Breadth-First Graph Traversal

Time Complexity: O(n + m) (visit each city and destination in worst case)
Space Complexity: O(n + m) (store each and every path in the worst case)

Process:
    - Create an undirected graph by having a weighted adjacency list store all the
      paths between cities and the travel times
    - Traverse the adjacency list from the origin city and perform
      breadth-first graph traversal until maximum time limit has been reached

Time Spent: 38 minutes
"""

from collections import defaultdict, deque

def vacation_destinations(destinations, origin, k):
    adj_list = defaultdict(list)
    output = []
    for c1, c2, time in destinations:
        adj_list[c1].append((c2, time))
        adj_list[c2].append((c1, time))

    q = deque([(origin, -1)])
    visited = {origin}
    while q:
        curr_city, time = q.popleft()

        if time <= k and time != -1:
            output.append(curr_city)

        for nbr, next_time in adj_list[curr_city]:
            if nbr not in visited:
                q.append((nbr, time+next_time+1))
                visited.add(nbr)

    return len(output)

def main():
    destinations = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5),
                    ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5),
                    ("Philadelphia", "Washington, D.C.", 2.5)]

    print(vacation_destinations(destinations, "New York", 5))
    # Correctly outputs 2 destinations

    print(vacation_destinations(destinations, "New York", 7))
    # Correctly outputs 4 destinations

    print(vacation_destinations(destinations, "New York", 8))
    # Correctly outputs 6 destinations

    destinations2 = [("Boston", "New York", 4), ("Houston", "Austin", 2)]

    print(vacation_destinations(destinations2, "New York", 2))
    # Correctly outputs 0 destinations

    print(vacation_destinations(destinations2, "Austin", 2))
    # Correctly outputs 1 destination

    print(vacation_destinations(destinations2, "Houston", 0))
    # Correctly outputs 0 destinations

main()
