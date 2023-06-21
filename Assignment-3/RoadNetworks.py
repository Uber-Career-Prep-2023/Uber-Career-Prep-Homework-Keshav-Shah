'''
Keshav Shah

Question 6: Road Networks
Given a list of towns and a list of pairs representing roads between towns, return the number of road networks.
(For example, a state in which all towns are connected by roads has 1 road network, and a state in which none of the
towns are connected by roads has 0 road networks.)

Depth-First Search

Time Complexity: O(V + E) (DFS at each vertex is at worst V + E at each node)
Space Complexity: O(V + E) (adjacency list will take up V + E space)

Process:
    - Create an adjacency list with the edges given and do DFS on the graph
      to visit all the nodes in the set
    - Count the number of connected components in the set as if DFS is applied
      to an unvisited vertex it is a new connected component or road network

Time Spent: 38 minutes
'''

def road_networks(towns, roads):

    # create adjacency list
    adj_list = {t: [] for t in towns}
    for road in roads:
        # since road is a tuple have separate variables for each town
        t1, t2 = road
        adj_list[t1].append(t2)
        adj_list[t2].append(t1)

    visited_towns = set()

    # dfs to check roads that are connected
    def dfs(road):
        visited_towns.add(road)
        for nbr in adj_list[road]:
            if nbr not in visited_towns:
                dfs(nbr)

    networks = 0

    for town in towns:
        if town not in visited_towns:
            dfs(town)
            networks += 1

    return networks

def main():
    towns = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    roads = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"),
             ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    print(road_networks(towns, roads)) # Correctly Outputs 3 Road Networks

    towns2 = ["Austin", "Houston", "New York"]
    roads2 = [("Houston", "Austin"), ("Austin", "Houston"), ("Houston", "New York")]
    print(road_networks(towns2, roads2)) # Correctly Outputs 1 Road Network

    towns3 = ["Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    roads3 = [("Kahului", "Hana"), ("Waimea", "Haiku"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    print(road_networks(towns3, roads3))  # Correctly Outputs 2 Road Networks

main()
