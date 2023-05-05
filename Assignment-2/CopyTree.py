'''
Keshav Shah

Question 4: CopyTree
Given a binary tree, create a deep copy. Return the root of the new tree.

Breadth First Search

Time Complexity: O(n)
Space Complexity: O(n)

Process:
    - use BFS and recursion to iterate through all nodes in the BST layer by layer to create the deep copy

Time Spent: 35 minutes
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def CopyTree(root):
    if not root:
        return None
    else:
        copy = Node(root.val)
        copy.left = CopyTree(root.left)
        copy.right = CopyTree(root.right)
        return copy

def generate_tree(tree, root):
    tree.append(root.val)
    if root.left:
        generate_tree(tree, root.left)
    if root.right:
        generate_tree(tree, root.right)
    return tree


def main():
    node1 = Node(4)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(1)
    node5 = Node(3)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    root = node1
    deep_copy = CopyTree(root)

    print(generate_tree([], deep_copy))  # Output: [4, 2, 1, 3, 6]
    print(generate_tree([], root))  # Output: [4, 2, 1, 3, 6]


main()
