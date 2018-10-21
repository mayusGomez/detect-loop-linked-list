Loop Detection on Linked List
==============================

A linked list contains a sequence of nodes, each node have two attributes: 

-   data: node's value
-   next: reference to next node

For example the linked list [5]--> [3] --> [8] --> [1] --> null:

    node1( value = 5, next = node2)
    node2( value = 3, next = node3)
    node3( value = 8, next = node4)
    node4( value = 1, next = null)

The linked list in this packages let add a new node with a recursive reference
(loop to a node in the middle) [5]--> [3] --> [8] --> [1] --> [8] ...:

    node1( value = 5, next = node2)
    node2( value = 3, next = node3)
    node3( value = 8, next = node4)
    node4( value = 1, next = node3)

This can cause a problem when we need traverse values. Then, it's necessary create a
function that let us identify this situation and avoid a infinite loop. For this
purpose one implementation is:

- Traverse all the nodes and store the hash value or memory id of each node, and when detect
  a value stored previously then return True for the loop.

Another function implementation is the 
[Floyd’s Cycle-Finding Algorithm](https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/), which 
traverse the linked list using two pointers, move one pointer by one and the 
other by two. When traverse the list until find a null reference, the function 
return False for indicating a found loop, each pointer's iterations evaluate 
if both pointers are the same and return True when this happens. This algorithm 
avoid the use of another structure like [Set](https://docs.python.org/3.6/tutorial/datastructures.html#sets) 
or [Dictionary](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries) for store the reference 
to previously nodes, this is the snippet:

```python
def detect_loop(self):
    slow_node = self.head  # This move by one
    fast_node = self.head  # This move by two
    while slow_node and fast_node and fast_node.next:
        # When no more nodes are found, then the linked list is free of loop
        slow_node = slow_node.next
        fast_node = fast_node.next.next
        if slow_node == fast_node: 
            # If the slow and fast node are the same, then linked list have a loop
            return True

    return False
```

Run the package
----------------

The linked_list package in this repo show the entire code, run this with the next instructions:

```python
from linked_list import LinkedList, LinkedListNode, LinkedListLoopException

# Create LinkedList instance and nodes
link_lst = LinkedList()
node1 = LinkedListNode(100)
node2 = LinkedListNode(90)
node3 = LinkedListNode(80)
node4 = LinkedListNode(70)
node5 = LinkedListNode(60)
node6 = LinkedListNode(50)

# Add nodes to LikedList
link_lst.insert(node1)
link_lst.insert(node2)
link_lst.insert(node3)
link_lst.insert(node4)
link_lst.insert(node5)
link_lst.insert(node6)
link_lst.insert(40)
link_lst.insert(30)
link_lst.insert(20)
link_lst.insert(10)

# Print the list
link_lst.print_list()

# Insert a loop
link_lst.insert(node3)

# Try print the list should raise a LinkedListLoopException
try:
    link_lst.print_list()
except LinkedListLoopException as e:
    print('Loop Error:{}'.format(e))
```