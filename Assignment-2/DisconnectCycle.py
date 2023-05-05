'''
Keshav Shah

Question 9: DisconnectCycle
Given a singly linked list, disconnect the cycle, if one exists.

Hashing Nodes of Linked List

Time Complexity: O(n) (traverse list to find cycle)
Space Complexity: O(n) (storing nodes in hashmap)

Process:
    - Store linked list nodes in hashmap
    - If current node's next does not already appear in hashmap there is no cycle, and store this node in the hashmap
    - Else if the current node's next appears in the hashmap there is a cycle, set current's next to null to
      end the cycle

Time Spent: 37 minutes
'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def disconnect_cycle(head):
    if not head:
        return None

    # hashmap to store visited nodes
    nodes = {}
    place = Node(0, head)
    current = head
    while current:
        if current.next not in nodes:
            nodes[current] = 1
            current = current.next
        else:
            current.next = None

    return place.next

def print_ll(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    for val in result:
        print(val, end=" | ")

def main():
    # create node 3 first to be able to reference it in the cycle
    node3 = Node(12)
    node6 = Node(4, node3)
    node5 = Node(11, node6)
    node4 = Node(9, node5)
    node3.next = node4
    node2 = Node(18, node3)
    node1 = Node(10, node2)

    # the below LL has an infinite loop due to cycle
    # print_ll(node1)

    disconnect_cycle(node1)
    print_ll(node1) # 10 | 18 | 12 | 9 | 11 | 4 | 

main()
