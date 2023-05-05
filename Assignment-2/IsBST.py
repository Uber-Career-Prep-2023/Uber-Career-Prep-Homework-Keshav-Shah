'''
Keshav Shah

Question 4: IsBST
Given a binary tree, determine if it is a binary search tree.

Breadth First Search

Time Complexity: O(n) worst case
Space Complexity: O(n)

Process:
    - compare current node to left node, if left node greater, return False
    - compare current node to right node, if right node smaller, return False
    - if both do not return False then call itself on left and right nodes and return True

Time Spent: 35 minutes
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class IsBST:
    def isValidBST(self, root):
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, node, left, right):
        if not node:
            return True
        if left > node.val or right < node.val:
            return False
        return (self.valid(node.left, left, node.val) and
                self.valid(node.right, node.val, right))

def main():
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(5)
    node1.left = node2
    node1.right = node3

    tree = IsBST()
    print(tree.isValidBST(node1))  # Output: True

    node4 = Node(100)
    node2.left = node4

    print(tree.isValidBST(node1))  # Output: False


main()
