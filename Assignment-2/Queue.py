"""
Keshav Shah

Queue

Implementation Complexity: O(n)
"""

class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    # Create various methods for class Queue
    def __init__(self):
        """
        Initialize the queue.
        """
        self._queue = []

    def peek(self):
        return self._queue[0]

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._queue)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        queue_string = ""
        for items in self._queue:
            queue_string += str(items) + " "
        return queue_string

    def enqueue(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._queue.append(item)

    def dequeue(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        return self._queue.pop(0)

    def isEmpty(self):
        return len(self._queue) == 0

    def clear(self):
        """
        Remove all items from the queue.
        """
        for _items in range(len(self._queue)):
            self._queue.pop(0)

def main():
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(15)
    q.dequeue()
    print(q) # expected 10 15, correct
    print(q.peek()) # expected 10, correct
    print(q.isEmpty()) # expected False, correct

main()
