# INTRODUCTION ABOUT LINKED LIST
'''
- A linked list is a linear data structure that consists of a series of nodes connected by pointers.
Each node contains data and a reference to the next node in the list.
_ It consists of nodes where each node contains data and a reference (link)
to the next node in a sequence.
_ Unlike array, it allows for dynamic memory allocation and efficient insertion and deletion 
opearions compared to arrays.

Linked List:
_ Data Structure non-contiguous
_ Dynamic memory allocation
_ Efficient Insertion and Deletion
- Sequential access

Array:
_ Data Structure contiguous
_ Static memory allocation
_ Inefficient Insertion and Deletion
_ Random access

'''

class Node:
    def __init__(self):
        self.data = None
        self.next = None

def insertAtFront(head_ref, new_data):
    # 1. Allocate node
    new_node = Node()

    # 2. Put in the data
    new_node.data = new_data

    # 3. Make next of new node as head
    new_node.next = head_ref

    # 4. Move the head to point to the new node
    head_ref = new_node

    return head_ref

def removeFirstNode(head):
    if not head:
        return None
    temp = head

    # Move the head pointer to the next node
    head = head.next
    temp = None
    return head

def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == '__main__':
    head = None
    head = insertAtFront(head, 6)
    head = insertAtFront(head, 5)
    head = insertAtFront(head, 4)
    head = insertAtFront(head, 3)
    head = insertAtFront(head, 2)
    head = insertAtFront(head, 1)
    print("After inserting nodes at the front: ", end = "")
    printList(head)

    head = removeFirstNode(head)
    print("After remove first node: ", end = "")
    printList(head)



