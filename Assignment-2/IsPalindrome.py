'''
Keshav Shah

Question 8: IsPalindrome
Given a doubly linked list, determine if it is a palindrome.

Doubly Linked List Forward-Backward Two Pointers

Time Complexity: O(2n) => O(n) (traverse list first and then check if palindrome)
Space Complexity: O(1)

Process:
    - Find middle of list
    - If list odd set left and right pointers to middle node
    - If list even set left pointer to 1st middle node and right pointer to second middle node
    - Move pointers outward, if left != right then return False
    - Return True if end of list is reached

Time Spent: 35 minutes
'''


class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def isPalindrome(head):
    if not head:
        return False

    # find length of LL
    current = head
    count = 1
    while current.next:
        count = count + 1
        current = current.next

    # calculate middle node
    middle = count // 2
    iter = 0
    left = head
    right = head

    while iter != middle:
        left = left.next
        right = right.next
        iter += 1

    if count % 2 == 0:
        # make left and right pointer different if list is even length
        left = left.prev

    # move the pointers outward
    while left and right:
        if left.val != right.val:
            return False
        left = left.prev
        right = right.next

    return True

def print_ll(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    for val in result:
        print(val, end=" | ")

def main():
    node6 = Node(6)
    node5 = Node(7, node6)
    node4 = Node(8, node5)
    node3 = Node(8, node4)
    node2 = Node(7, node3)
    node1 = Node(6, node2, None)

    node6.prev = node5
    node5.prev = node4
    node4.prev = node3
    node3.prev = node2
    node2.prev = node1

    print_ll(node1)
    print(isPalindrome(node1)) # 6 | 7 | 8 | 8 | 7 | 6 | True

    node11 = Node(9)
    node10 = Node(2, node11)
    node9 = Node(4, node10)
    node8 = Node(12, node9)
    node7 = Node(9, node8, None)

    node11.prev = node10
    node10.prev = node9
    node9.prev = node8
    node8.prev = node7

    print_ll(node7)
    print(isPalindrome(node7)) # 9 | 12 | 4 | 2 | 9 | False

main()
