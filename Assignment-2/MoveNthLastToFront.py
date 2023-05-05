'''
Keshav Shah

Question 7: MoveNthLastToFront
Given a singly linked list, move the nth from the last element to the front of the list.

Linked List Fixed-Distance Two Pointers

Time Complexity: O(2n) => O(n) (traverse list and then make the alteration)
Space Complexity: O(1)

Process:
    - Calculate length of LL by traversing it
    - To find the nth node, subtract the length of the LL by n
    - Set the current node pointer to the nth node and the previous node pointer to the node before
    - Set the previous nodes next to the current nodes next and the nth nodes next to the head node

Time Spent: 35 minutes
'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def move_nth_to_front(head, n):
    if not head:
        return None

    # find length of list first
    current = head
    count = 1
    while current.next:
        count = count + 1
        current = current.next

    # out of bounds
    if n > count:
        return None

    iter = 0
    delete = count - n
    place = Node(0)
    place.next = head
    previous = place
    current = head
    while iter != delete:
        iter += 1
        previous = current
        current = current.next

    # do the swap as we are now at the correct location in the LL
    previous.next = current.next
    current.next = head
    return current

def print_ll(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    for val in result:
        print(val, end=" | ")

def main():
    node9 = Node(19)
    node8 = Node(6, node9)
    node7 = Node(11, node8)
    node6 = Node(9, node7)
    node5 = Node(20, node6)
    node4 = Node(7, node5)
    node3 = Node(8, node4)
    node2 = Node(2, node3)
    node1 = Node(15, node2)

    print_ll(node1)   # Output: | 15 | 2 | 8 | 7 | 20 | 9 | 11 | 6 | 19 |
    new_list1 = move_nth_to_front(node1, 2) # Output: | 6 | 15 | 2 | 8 | 7 | 20 | 9 | 11 | 19 |
    new_list2 = move_nth_to_front(node1, 7) # Output: | 8 | 15 | 2 | 7 | 20 | 9 | 11 | 6 | 19 |
    print_ll(new_list1)
    print_ll(new_list2)

main()
