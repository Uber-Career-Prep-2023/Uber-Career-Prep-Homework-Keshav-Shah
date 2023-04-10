"""
Keshav Shah

Singly Linked List

Implementation Complexity: O(n)
"""

class Node:

    # Initialize Node object
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:

    # Initialize Linked List Object
    def __init__(self):
        self.head = None

    # creates new Node with data val at front; returns new head
    def insertAtFront(self, val):
        node_head = Node(val)
        node_head.next = self.head
        self.head = node_head
        return node_head

    # creates new Node with data val at end
    def insertAtBack(self, val):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(val)

    # creates new Node with data val after Node loc
    def insertAfter(self, val, loc):
        current = self.head
        new_node = Node(val)
        while current is not None:
            if current == loc:
                new_node.next = current.next
                current.next = new_node
            current = current.next

    # removes first Node; returns new head
    def deleteFront(self):
        if self.head is None:
            return None
        else:
            node_head = self.head.next
            self.head = node_head
            return node_head

    # removes last Node
    def deleteBack(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            return None
        else:
            previous = None
            current = self.head
            while current.next is not None:
                previous = current
                current = current.next
            if previous is not None:
                previous.next = None
            else:
                self.head = None

    # deletes Node loc; returns head
    def deleteNode(self, loc):
        if loc == self.head:
            return self.deleteFront()
        previous = None
        current = self.head
        while current is not loc:
            previous = current
            current = current.next
        next = current.next
        previous.next = current

    # int length(Node head) // returns length of the list
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.next
        return count

    # reverses the linked list iteratively
    def reverseIterative(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        return previous


    # helper function for reverseRecursive
    def reverseRecursiveHelper(self, head):
        if head.next is None:
            self.head = head
            return head
        node = self.reverseRecursiveHelper(head.next)
        node.next = head
        head.next = None
        return head

    # reverses the linked list recursively (Hint: you will need a helper function)
    def reverseRecursive(self):
        if self.head is None or self.head.next is None:
            return self.head
        self.reverseRecursiveHelper(self.head)
        return self.head

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(str(current.val))
            current = current.next
        nodes.append("None")
        return " -> ".join(nodes)

def main():
    list = SinglyLinkedList()
    list.insertAtFront(1)
    list.insertAtFront(2)
    list.insertAtFront(3)
    list.insertAtFront(10)
    list.insertAtBack(11)
    list.reverseIterative()
    list.reverseRecursive()
    list.deleteFront()
    list.deleteBack()
    # expected output: 3 -> 2 -> 1 -> None, functions indeed return this output
    print(list)

main()

