"""
Keshav Shah

Binary Search Tree

Implementation Complexity: O(n)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def min(self):
        if not self.left:
            return None
        current = self.left
        while current.left:
            current = current.left
        return current.val

    def max(self):
        if not self.right:
            return None
        current = self.right
        while current.right:
            current = current.right
        return current.val

    def contains(self, val):
        if val < self.val:
            if not self.left:
                return False
            else:
                return self.left.contains(val)
        elif val > self.val:
            if not self.right:
                return False
            else:
                return self.right.contains(val)
        else:
            return True

    def insert(self, val):
        if val < self.val:
            if not self.left:
                self.left = BST(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if not self.right:
                self.right = BST(val)
            else:
                self.right.insert(val)

    def delete(self, val):
        if val < self.val:
            if not self.left:
                return None
            else:
                self.left = self.left.delete(val)
        elif val > self.val:
            if not self.right:
                return None
            else:
                self.right = self.right.delete(val)
        else:
            if not self.right:
                return self.left
            elif not self.left:
                return self.right
            else:
                current = self.right
                while current.left:
                    current = current.left
                self.val = current.val
                self.right = self.right.delete(current.val)
        return self

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.val)
        if self.right:
            self.right.inorder_traversal()

        return ""

def main():
    bst = BST(7)
    print(bst.inorder_traversal()) # correctly outputs root node 7 only
    bst.insert(5)
    bst.insert(10)
    bst.insert(2)
    print(bst.inorder_traversal()) # correctly returns in order traversal of bst after insertion [2,5,7,10]
    bst.delete(2)
    print(bst.inorder_traversal()) # correctly outputs in order traversal after deleting node [5,7,10]
    print(bst.min()) # correctly prints 5
    print(bst.max()) # correctly prints 10
    print(bst.contains(7)) # correctly prints True
    print(bst.contains(22)) # correctly prints False

main()
