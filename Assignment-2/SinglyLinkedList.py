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
        while current is not None:
            if current == loc:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            previous = current
            current = current.next
        return self.head                

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
    linked_list = SinglyLinkedList()
    linked_list.insertAtFront(1)
    linked_list.insertAtFront(2)
    linked_list.insertAtFront(3)
    linked_list.insertAtFront(10)
    linked_list.insertAtBack(11)
    linked_list.reverseIterative()
    linked_list.reverseRecursive()

    print("Initial linked list:")
    print(linked_list)

    linked_list.deleteFront()
    linked_list.deleteBack()
    print("Linked list after deleting front and back nodes:")
    print(linked_list)

    # This now correctly implemented the deleteNode method
    node_to_delete = linked_list.head.next
    linked_list.deleteNode(node_to_delete)
    print("Linked list after deleting node:", node_to_delete.val)
    print(linked_list)

main()

