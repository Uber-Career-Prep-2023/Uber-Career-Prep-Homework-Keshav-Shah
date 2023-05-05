'''
Keshav Shah

Question 6: DedupSortedList
Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

Linked List Fixed-Distance Two Pointers

Time Complexity: O(n) worst case
Space Complexity: O(1)

Process:
    - Set the previous pointer to a placeholder node and current node to the head of the node
    - If previous = current move current forward let us move forward and remove the duplicate
    - Otherwise let us move previous and current forwards together
    - This method works since the LL is sorted

Time Spent: 35 minutes
'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def dedup_sorted_list(head):
    if not head:
        return None

    place = Node()
    place.next = head
    prev, current = place, head

    while current:
        if prev.val == current.val:
            prev.next = current.next
        else:
            prev = current
        current = current.next

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
    node9 = Node(10)
    node8 = Node(10, node9)
    node7 = Node(5, node8)
    node6 = Node(5, node7)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(2, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    print_ll(node1)  # Output: | 1 | 2 | 2 | 4 | 5 | 5 | 5 | 10 | 10 |
    print_ll(dedup_sorted_list(node1))  # Output: | 1 | 2 | 4 | 5 | 10 |

    node13 = Node(8)
    node12 = Node(8, node13)
    node11 = Node(8, node12)
    node10 = Node(8, node11)

    print_ll(node10)  # Output: | 8 | 8 | 8 | 8 |
    print_ll(dedup_sorted_list(node10))  # Output: | 8 |


main()
