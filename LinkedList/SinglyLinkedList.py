# Singly Linked List
'''
_ A singly linked list is a linear data structure in which the elements are not 
stored in contiguous memory locations and each element is connected only to its 
element using a pointer.
_ The data part stores the information and the next pointer points to the next node
_ The next pointer of the last node stores null as it is the last node of the linked list
and there is no next node.

      Head
        |
        A   ... -> B ... -> C... -> D... -> NULL
       Data Next 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None