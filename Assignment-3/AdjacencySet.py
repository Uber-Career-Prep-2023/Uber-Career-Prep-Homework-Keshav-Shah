"""
Keshav Shah

Adjacency Set Representation of a Graph

Approach: If we see that any particular node, either the source node or the node to
be reached does not exit in the set, initialize it with an empty list
"""

from collections import deque

# time complexity and space complexity: O(n)
def adjacencySet(edges):
    graph = {}
    for node1, node2 in edges:
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)

    return graph

# bfs algorithm to check if there is a path from the start node to target node
# time complexity O(V+E), space complexity: O(V)
def bfs(start, target, neighbors):
    q = deque([start])
    visited = set([start])
    while q:
        curr = q.popleft()
        if curr == target:
            return True
        for neighbor in neighbors[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return False

# dfs algorithm to check if there is a path from the start node to target node
# time complexity O(V+E), space complexity: O(V)
def dfs(start, target, neighbors):
    s = [start]
    visited = set([start])
    while s:
        curr = s.pop()
        if curr == target:
            return True
        for neighbor in neighbors[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                s.append(neighbor)
    return False

# method: first count the in-degree of each node, find the nodes with 0 in-degree and pop those nodes, then add the
# rest of the additional nodes in the correct topological ordering
# time complexity O(V+E), space complexity: O(V)
def topologicalSort(graph):
    # calculating in-degrees
    in_degrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degrees[neighbor] += 1

    # finding 0 in-degree nodes
    zero_indegree = []
    for node in in_degrees:
        if in_degrees[node] == 0:
            zero_indegree.append(node)

    # pop nodes from the zero-indegree list
    topological_sorted_order = []
    while len(zero_indegree) > 0:
        node = zero_indegree.pop()
        topological_sorted_order.append(node)
        for nbr in graph[node]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                zero_indegree.append(nbr)

    return topological_sorted_order

def main():
    # testing adjacencySet function
    graph_edges = [(1, 2), (2, 3), (1, 3), (3, 2), (4, 5)]
    graph_adjacency_set = adjacencySet(graph_edges)
    print(graph_adjacency_set) # Output is {1: [2, 3], 2: [3], 3: [2], 4: [5], 5: []} as expected

    # testing bfs
    print(bfs(1, 2, graph_adjacency_set)) # Output is True as there is a path from 1 to 2
    print(bfs(3, 4, graph_adjacency_set)) # Output is False as there is no path from 3 to 4
    print(bfs(1, 3, graph_adjacency_set)) # Output is True as there is a path from 1 to 3

    # testing dfs
    print(dfs(2, 2, graph_adjacency_set)) # Output is True as there is a path from the node 2 back to node 2
    print(dfs(3, 2, graph_adjacency_set)) # Output is True as there is a path from node 3 to node 2
    print(dfs(1, 4, graph_adjacency_set)) # Output is False as there is no path from node 1 to node 4

    # testing a topological ordering of a graph
    graph_edges_input = [(1, 2), (2, 3), (1, 3), (3, 4), (3, 5), (4, 5), (2, 4)]
    graph_input = adjacencySet(graph_edges_input)
    # print(graph_input)
    print(topologicalSort(graph_input)) # topological ordering output is [1,2,3,4,5] as expected
    graph_edges2 = [(1, 5), (2, 3), (1, 3), (3, 4), (4, 5)]
    graph_input2 = adjacencySet(graph_edges2)
    # print(graph_input2)
    print(topologicalSort(graph_input2)) # topological ordering output is [2,1,3,4,5] as expected

main()
