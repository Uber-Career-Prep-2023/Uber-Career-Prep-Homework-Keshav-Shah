import collections

'''
Keshav Shah

Question 10: LeftView
Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.

Level Order (Breadth-First) Traversal

Time Complexity: O(n) (add all nodes to queue)
Space Complexity: O(n) (tree size)

Process:
    - Create queue with root node
    - For length of queue, pop leftmost node and add the right child and then left child and add these nodes to output

Time Spent: 39 minutes
'''


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_view(root):
    if not root:
        return None

    result = []
    # create a double sided queue
    queue = collections.deque([root])

    while queue:
        ls = None
        for iter in range(len(queue)):
            node = queue.popleft()
            if node:
                ls = node
                queue.append(node.right)
                queue.append(node.left)
        if ls:
            result.append(ls.val)

    return result

def main():
    node15 = Node(15)
    node14 = Node(14, None, node15)
    node13 = Node(13, node14, None)
    node20 = Node(20)
    node9 = Node(9, node20, None)
    node3 = Node(3, node9, node13)
    node8 = Node(8)
    root = Node(7, node8, node3)

    print(left_view(root)) # Output: [7, 8, 9, 20, 15]

main()
