# Linked List
### What is Linked List ?
- A linked list is a linear data structure that consists of a series of nodes connected by pointers. Each node contains data and a reference to the next node in the list.
- It consists of nodes where each node contains data and a reference (link)to the next node in a sequence.
- Unlike array, it allows for dynamic memory allocation and efficient insertion and deletion opearions compared to arrays.

#### Linked List:
+ Data Structure non-contiguous
+ Dynamic memory allocation
+ Efficient Insertion and Deletion
+ Sequential access

#### Array:
+ Data Structure contiguous
+ Static memory allocation
+ Inefficient Insertion and Deletion
+ Random access


# Singly Linked List
- A singly linked list is a linear data structure in which the elements are not stored in contiguous memory locations and each element is connected only to its element using a pointer.
- The data part stores the information and the next pointer points to the next node
- The next pointer of the last node stores null as it is the last node of the linked list and there is no next node.
```
      Head
        |
        A   ... -> B ... -> C... -> D... -> NULL
       Data Next 
```

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

```

### Insert a Node after a Given Node
To insert a node after a given node:
+ Check if the given node exists or not
+ If it don't exist -> Terminate the process
+ If the given node exist ->
    ```
    1. Make the element to be inserted as a new node
    2. Change the next pointer of a given node to the new node
    3. Now shift the original next pointer of given node to the next pointer of new node
    ```

```
def insertAfter(self, prev_node, new_data):
    # 1. Check if the given prev_node exists
    if prev_node is None:
        print("The given prev node must in linked list")
        return
    # 2. Create new node and put in the data
    new_node = Node(new_data)

    # 3. Make next of new Node as next of prev_node
    new_node.next = prev_node.next

    # 4. Make next of prev_node as new_node
    prev_node.next = new_node

```

### Insert a Node at the end
To insert a node at the end:
   + Go to the last node
   + Change the next pointer of last node from NULL to new node
   + Make the next pointer of new node as NULL to show the end

```
def append(self, new_data):
    # 1. Create new node, put in the data and set next of None
    new_node = Node(new_data)

    # 2. If the linked list is empty, then make the new node as head
    if self.head is None:
        self.head = new_node
        return
    
    # 3. Else traverse till the last node
    last = self.head
    while (last.next):
        last = last.next
    
    # 4. Change the next of last node
    last.next = new_node

```

### Find the middle of the Linked List
```
def getMiddle(head):
    ans = []
    
    while head is not None:
        ans.append(head.data)
        head = head.next
    
    mid = len(ans) // 2
    
    return ans[mid]
```

### Reverse a Linked List
```
def reverse(self):
    prev = None
    curr = self.head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    self.head = prev

```

### Delete last occurence
```
def deleteLast(head, x):
    curr = head
    point = None
    
    while curr is not None:
        # If found key, update 
        if curr.data == x:
            point = curr
        curr = curr.next
    
    # If the last occurrence is the last node 
    if point is not None and point.next is None:
        curr = head
        while curr.next != point:
            curr = curr.next
        curr.next = None
    
    # If it is not the last node 
    if point != None and point.next != None:
        point.data = point.next.data
        curr = point.next
        point.next = point.next.next
        
    return head
```