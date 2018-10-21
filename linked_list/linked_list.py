"""Linked List, let to insert nodes and print the list, raise LinkedListLoop exception when detect a loop"""
from .exceptions import LinkedListLoopException


class LinkedListNode:
    """Node class, two attributes:
        - data: node's value
        - next: next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList class, let insert a node at the beginning of the list, and let print the list"""
    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert a value as a node at the beginning of the list, if the value is instance of
        LinkedListNode just insert the new node """

        if not isinstance(value, LinkedListNode):
            value = LinkedListNode(value)

        value.next = self.head
        self.head = value

    def print_list(self):
        """Print linked lists values, when detect a loop raise an Exception"""
        if self.detect_loop():
            raise LinkedListLoopException("It's not possible print the Linked List, loop detected")

        node = self.head
        while node:
            print('Node[{}]-->'.format(node.data))
            node = node.next

    def detect_loop(self):
        """Evaluate the list to find loop, implementation of Floyd’s Cycle-Finding Algorithm
        source: https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/, this implementation
        avoids storing the nodes through which it has been passed.

        Return True when find a loop, False in otherwise
        """
        slow_node = self.head
        fast_node = self.head
        while slow_node and fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                return True

        return False

