class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = None

'''
1. Write a function, linkedListValues, that takes in the head of a linked list as an argument. 
The function should return an array containing all values of the nodes in the linked list.
'''
# def linkedListValues(head):
'''
    values = []
    curr = head
    while curr:
        values.append(curr.data)
        curr = curr.next
    return values
'''
    # values = []
    # fillValues(head, values)
    # return values
'''
def fillValues(head, values):
    if head is None:
        return   
    values.append(head.data)
    fillValues(head.next, values)
'''
'''
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c 
c.next = d

print(linkedListValues(a))
'''

##########################################################################################

'''
2. Write a function, sumList, that takes in the head of a linked list containing numbers as 
an argument. The function should return the total sum of all values in the linked list.

'''
'''
def sumList(head):
    values = []
    curr = head
    while curr:
        values.append(curr.data)
        curr = curr.next
    
    return sum(values)
'''
'''
def sumList(head):
    if head is None: return 0
    return head.data + sumList(head.next)

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7);

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sumList(a)) # 19
'''
##########################################################################################
'''
3. Write a function, linkedListFind, that takes in the head of a linked list and a target value.
The function should return a boolean indicating whether or not the linked list contains the target.
'''
'''
def linkedListFind(head, target):
    curr = head
    while curr:
        if curr.data == target:
            return True
        curr = curr.next
    
    return False
'''
'''
def linkedListFind(head, target):
    if head is None: return False
    if head.data == target: return True
    return linkedListFind(head.next, target)

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c 
c.next = d

print(linkedListFind(a, 'D'))
'''

##########################################################################################

'''
4. Write a function, reverseList, that takes in the head of a linked list as an argument. 
The function should reverse the order of the nodes in the linked list in-place and return 
the new head of the reversed linked list.

'''
'''
def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev
'''
def reverseList(head, prev=None):
    if head is None: return prev
    next_node = head.next
    head.next = prev
    return reverseList(next_node, head)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverseList(a)) # f -> e -> d -> c -> b -> a
