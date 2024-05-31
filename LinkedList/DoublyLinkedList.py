# Doubly Linked List
'''
_ Doubly Linked List is a type of linked list where each node has 3 parts: data, next and previous
_ The data stores the information, the next points to the next node, the previous points to the 
previous node of the linked list
_ The next pointer of the last node and the previous pointer of the first node stores null

          Head
           |
    ...    A   ... -> B ... -> C... -> D... -> NULL
    NULL  Data Next 

'''
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

'''
Advantages:
+ Can be traversed in both forward and backward directions.
+ The delete operation in DLL is more efficient if a ptr to the node
to be deleted is given
+ Quickly insert a new node before a given node
+ In SLL, to delete a node, a ptr to the previous is needed, to get the prev
node, sometimes the list is traversed. But in DLL, we can get the prev node
using the prev ptr.

Disavantages:
+ Every node of DLL requires extra space for a prev ptr.
+ All operation require an extra ptr prev to be maintained.
'''

# Insert at the beginning
'''
1. Allocate memory for a new node and assign the provided value to its data field
2. Set the prev ptr of the new_node to None
3. If the list is empty: 
    + Set the next ptr of the new_node to None
    + Update the head ptr to point to the new_node
4. If the list is not empty:
    + Set the next ptr of the new_node to the current head
    + Update the prev ptr of the current head to point to the new_node
    + Update the head pointer to point to new_node
'''
def push(self, new_data):
    # 1 & 2: Allocate the Node and put in the data
    new_node = Node(data = new_data)

    # 3. Make next of new node as head and previous as None
    new_node.next = self.head
    new_node.prev = None

    # 4. Change prev of head node to new node
    if self.head is not None:
        self.head.prev = new_node
    
    # 5. Move the head to point to the new node
    self.head = new_node


# Insert between two nodes
'''
1. Add a node after a given node
+ First, create a new_node
+ Now insert the data in the new_node
+ Point the next of new_node ot the next of previous node
+ Point the next of previous node to new_node
+ Point the previous of new_node to previous node
+ Point the previous of next of new_node to new_node
'''
def insertAfter(self, prev_node, new_data):
    # Check if the given prev_node is None
    if prev_node is None:
        print("This node doesnt exist in list")
        return
    
    # 1. Allocate node and put in the data
    new_node = Node(data = new_data)

    # 2. Make next of new_node as next of prev_node
    new_node.next = prev_node.next

    # 3. Make the next of prev_node as new_node
    prev_node.next = new_node

    # 4. Make prev_node as previous of new_node
    new_node.prev = prev_node

    # 5. Change previous of new_node's next node
    if new_node.next is not None:
        new_node.next.prev = new_node

'''
2. Add a node before a given node
+ Allocate memory for a new_node
+ Put the data in new_node
+ Set the previous pointer of this new_node as the previous node of the next_node
+ Set the previous pointer of the next_node as the new_node
+ Set the next pointer of this new_node as the next_node
+ Set the next pointer of the previous of new_node to new_node
'''
def insertAfter(self, next_node, new_data):
    # Check if the given next_node is None
    if next_node is None:
        print("This node doesnt exist in list")
        return
    
    # 1. Allocate node and put in the data
    new_node = Node(data = new_data)

    # 2. Make previous of new node as previous of prev_node
    new_node.prev = next_node.prev

    # 3. Make previous of next_node as new_node
    next_node.next = new_node

    # 4. Make next_node as next of new_node
    new_node.next = new_node

    # 5. Change next of new_node's previous node
    if new_node.prev is not None:
        new_node.prev.next = new_node
    else:
        head = new_node

'''
3. Insertion at the end
+ Create a new_node
+ Put the value in the new_node
+ Make the next ptr of new_node as None
+ If the list is empty, make new_node as the head
+ Otherwise, travel to the end of the linked list
+ Now make the next pointer of the last node point to new_node
+ Change the previous pointer of new_node tot he last node of the list
'''
def append(self, new_data):
    # 1. Allocate node and put in the data
    new_node = Node(data = new_data)
    last = self.head

    # 2. This new_node is going to be the last node, so make the next of it as None
    new_node.next = None

    # 3. Af the LL is empty, then make the new_node as head
    if self.head is None:
        new_node.prev = None
        self.head = new_node
        return

    # 4. Else traverse till the last node
    while (last.next is not None):
        last = last.next
    
    # 5. Change the next of last node
    last.next = new_node

    # 6. Make last node as previous of new node
    new_node.prev = last


# Reverse
def reverse(self):
    temp = None
    current = self.head
 
    # Swap next and prev for all nodes of doubly linked list
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
 
    # Before changing head, check for the cases like empty list and list with only one node
    if temp is not None:
        self.head = temp.prev