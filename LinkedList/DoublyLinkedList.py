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