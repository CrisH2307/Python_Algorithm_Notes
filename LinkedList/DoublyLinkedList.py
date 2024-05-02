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
    