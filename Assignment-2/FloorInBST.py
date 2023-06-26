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
    def __init__(self, data=0, left=None, right=None):
        self.key = data
        self.left = left
        self.right = right

def floor_in_bst(root, input):
    # Base cases
    if root == None:
        return -1
    if root.key == input:
        return input

    # If root's value is smaller, try in
    # right subtree
    elif root.key < input:
        k = floor_in_bst(root.right, input)
        if k == -1:
            return root.key
        else:
            return k

    # If root's key is greater, return
    # value from left subtree.
    elif root.key > input:
        return floor_in_bst(root.left, input)

def main():
    node20 = Node(20, None, None)
    node17 = Node(17, None, node20)
    node13 = Node(13, None, None)
    node16 = Node(16, node13, node17)
    node9 = Node(9, None, None)
    node8 = Node(8, None, node9)
    root = Node(10, node8, node16)

    print(floor_in_bst(root, 13)) # Floor : 13
    print(floor_in_bst(root, 15)) # Floor : 13

    # Convoluted BST test case
    node13 = Node(13, None, None)
    node16 = Node(16, None, None)
    node14 = Node(14, node13, None)
    node15 = Node(15, node14, node16)
    node20 = Node(20, node15, None)
    node0 = Node(2, None, None)
    root = Node(10, node0, node20)

    print(floor_in_bst(root, 13)) # Floor : 13
    print(floor_in_bst(root, 19)) # Floor : 16
    print(floor_in_bst(root, 17)) # Floor : 16
    print(floor_in_bst(root, 9)) # Floor : 2
    print(floor_in_bst(root, 1)) # Floor : Not existent so -1 returned

main()
