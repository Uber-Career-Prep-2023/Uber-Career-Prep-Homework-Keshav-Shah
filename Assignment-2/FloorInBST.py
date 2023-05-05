'''
Keshav Shah

Question 11: FloorInBST
Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal
to the target) in the BST.

Searching Binary Search Tree

Time Complexity: O(log n) (search left side of tree)
Space Complexity: O(1)

Process:
    - Check base case (invalid and leaf nodes)
    - if node equals target it is the greatest element and return it
    - if node greater than target, traverse left subtree to find lesser value
    - if node less than target traverse right subtree to find greater value

Time Spent: 38 minutes
'''

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def floor_in_bst(node, target):
    if not node:
        return -1

    if not node.left and not node.right:
        return node.val

    if node.val == target:
        return node.val

    # traverse left subtree
    elif node.val > target:
        return floor_in_bst(node.left, target)

    # traverse right subtree
    elif node.val < target:
        return floor_in_bst(node.right, target)

def main():
    node20 = Node(20, None, None)
    node17 = Node(17, None, node20)
    node13 = Node(13, None, None)
    node16 = Node(16, node13, node17)
    node9 = (9, None, None)
    node8 = (8, None, node9)
    root = Node(10, node8, node16)

    print(floor_in_bst(root, 13)) # Floor : 13
    print(floor_in_bst(root, 15)) # Floor : 13

main()
