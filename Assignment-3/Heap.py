"""
Keshav Shah

Heap Representation

"""

class Heap:
    def __init__(self):
        self.heap = []

    def top(self):
        if not self.heap:
            return None
        return self.heap[0]

    # utilize a heapify helper method to heapify the array after a new value is added to the heap
    # O(log n) complexity
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up()

    def heapify_up(self):
        child = len(self.heap) - 1
        parent = (child - 1) // 2

        while parent >= 0 and self.heap[child] <= self.heap[parent]:
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
        min_index = index
        left = 2*index + 1
        right = 2*index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self.heapify_down(min_index)

    # for testing
    def heap_output(self):
        return self.heap

def main():
    heap = Heap()
    heap.insert(10)
    heap.insert(8)
    heap.insert(7)
    heap.insert(12)
    heap.insert(5)
    print(heap.heap_output()) # heap is correctly outputted as [5, 7, 8, 12, 10]
    print(heap.top()) # the correct minimum value is outputted as 5

    heap.remove()
    print(heap.heap_output()) # heap is correctly outputted as [7,10,8,12]
    print(heap.top())  # minimum value is correctly 7
    heap.remove()
    print(heap.heap_output()) # heap is correctly outputted as [8,10,12]
    print(heap.top()) # minimum value is correctly 8

main()
