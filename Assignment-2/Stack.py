"""
Keshav Shah

Stack

Implementation Complexity: O(n)
"""

class Stack:
    """
    A simple implementation of a LIFO stack.
    """
    # Create various methods for class Stack
    def __init__(self):
        """
        Initialize the stack.
        """
        self._stack = []

    def top(self):
        return self._stack[-1]

    def __len__(self):
        """
        Returns: an integer representing the number of items in the stack.
        """
        return len(self._stack)

    def __str__(self):
        """
        Returns: a string representation of the stack.
        """
        return str(self._stack)

    def push(self, item):
        """
        Add item to the stack.

        input:
            - item: any data type that's valid in a list
        """
        self._stack.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        return self._stack.pop(len(self._stack) - 1)

    def isEmpty(self):
        return len(self._stack) == 0

    def clear(self):
        """
        Remove all items from the stack.
        """
        for _items in range(len(self._stack)):
            self._stack.pop(0)

def main():
    s = Stack()
    s.push(3)
    s.push(6)
    s.push(9)
    s.push(12)
    s.pop()
    print(s) # expected 3 6 9, correct
    print(s.top()) # expected 9, correct
    print(s.isEmpty()) # expected False, correct

main()
