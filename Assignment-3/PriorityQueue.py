"""
Keshav Shah

Priority Queue Representation

"""

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def top(self):
        if not self.heap:
            return None
        # returns the highest priority element
        return max(self.heap, key=lambda x: x[1])

    # utilize a heapify helper method to heapify the array after a new value is added to the heap
    # O(log n) complexity
    def insert(self, element, priority):
        self.heap.append((element, priority))
        self.heapify_up()

    def heapify_up(self):
        child = len(self.heap) - 1
        parent = (child - 1) // 2

        while parent >= 0 and self.heap[child][1] > self.heap[parent][1]:
            # complete a proper swap
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child, parent = parent, (child-1)//2

    # remove the top or minimum element in the heap
    # O(log n) complexity
    def remove(self):
        # swap minimum method for last value so that minimum value can be popped
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapify_down(0)

    def heapify_down(self, index):
        largest = index
        left = 2*index + 1
        right = 2*index + 2

        if left < len(self.heap) and self.heap[left][1] > self.heap[largest][1]:
            largest = left

        if right < len(self.heap) and self.heap[right][1] > self.heap[largest][1]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    # for testing
    def pq_output(self):
        return self.heap

def main():
    pq = PriorityQueue()
    pq.insert("A", 4)
    pq.insert("B", 8)
    pq.insert("C", 2)
    pq.insert("D", 1)
    pq.insert("E", 3)
    print(pq.pq_output()) # pq is correctly outputted as [('B', 8), ('A', 4), ('C', 2), ('D', 1), ('E', 3)]
    print(pq.top()) # the correct top value is outputted as ('B', 8)

    pq.remove()
    print(pq.pq_output()) # pq is correctly outputted as [('A', 4), ('E', 3), ('C', 2), ('D', 1)]
    print(pq.top())  # the correct top value is outputted as ('A', 4)
    pq.remove()
    print(pq.pq_output()) # pq is correctly outputted as [('E', 3), ('D', 1), ('C', 2)]
    print(pq.top()) # the correct top value is outputted as ('E', 3)

main()
