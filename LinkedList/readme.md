# Linked List
### What is Linked List ?
- A linked list is a linear data structure that consists of a series of nodes connected by pointers. Each node contains data and a reference to the next node in the list.
- It consists of nodes where each node contains data and a reference (link)to the next node in a sequence.
- Unlike array, it allows for dynamic memory allocation and efficient insertion and deletion opearions compared to arrays.
![](https://cdn.devdojo.com/images/june2021/linkedlist-insertfromback1.gif)

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

# Leetcode Pattern Problem
Linked list problems often feel tricky because we can only move **forward** and we work with **pointers**, not indices.  
But almost every problem boils down to a few common techniques.

---

## 1. Head & Tail Dummy Nodes
### Idea:
- Create a **dummy head** (before real head) or **dummy tail** (after real tail).
- Makes insertions/deletions easier, avoids special cases at boundaries.

### Common Use:
- **Design Linked List** (LeetCode 707)
- **LRU Cache** (LeetCode 146, using a doubly linked list)

---

## 2. Find the Middle (Fast & Slow Pointers)
### Idea:
- Use two pointers:
  - `slow` moves 1 step
  - `fast` moves 2 steps
- When `fast` hits the end, `slow` is at the middle.

### Common Use:
- **Palindrome Linked List** (LeetCode 234)
- **Reorder List** (LeetCode 143)
- **Maximum Twin Sum** (LeetCode 2130)

---

## 3. Reverse a Linked List (Full or Partial)
### Idea:
- Iteratively change `curr.next` to point to `prev`.
- Can reverse the whole list, or just a segment.

### Common Use:
- **Reverse Linked List** (LeetCode 206) → whole list
- **Reverse Linked List II** (LeetCode 92) → partial segment
- As a sub-step in problems like Palindrome check or Twin Sum

---

## 4. Reverse the Second Half
### Idea:
- Find the middle.
- Reverse the second half.
- Now you can walk from start and from (reversed) end simultaneously.

### Common Use:
- **Palindrome Linked List** (LeetCode 234)
- **Reorder List** (LeetCode 143)
- **Maximum Twin Sum** (LeetCode 2130)

---

## 5. Two Pointers, Same Speed (Different Starts)
### Idea:
- Start two pointers at different nodes, move both forward 1 step until they meet.

### Common Use:
- **Intersection of Two Linked Lists** (LeetCode 160)
- **Cycle detection phase 2** (LeetCode 142) → finding cycle entry after detection
- Comparing two halves after reverse (Palindrome, Twin Sum)

---

## 6. Two Pointers, Different Speed
### Idea:
- `fast` moves 2 steps, `slow` moves 1 step.
- Useful for detecting cycles or finding the middle.

### Common Use:
- **Linked List Cycle** (LeetCode 141)
- **Linked List Cycle II** (LeetCode 142)
- **Find Middle** for Palindrome / Reorder / Twin Sum

---

## 7. Two Pointers From Opposite Ends
### Idea:
- In arrays → easy (`i=0`, `j=n-1`).  
- In linked list → simulate using **reverse second half** or copy to array.

### Common Use:
- **Two Sum II (sorted array)** (LeetCode 167)
- In linked list → used indirectly for Palindrome / Twin Sum

---

## 8. Traversal Tricks
### Single traversal:
- While loop until `node is None`.
- Count length, find max/min, etc.

### Double traversal:
- First pass to get length.
- Second pass to reach a specific index.

### Common Use:
- **Remove Nth Node from End** (LeetCode 19) → either 2 passes, or 1 pass with fast/slow.

---

# Summary Table

| Technique                   | Example Problems                             |
|------------------------------|----------------------------------------------|
| Dummy Head/Tail              | Design Linked List (707), LRU Cache (146)   |
| Find Middle (fast/slow)      | Palindrome (234), Reorder List (143), Twin Sum (2130) |
| Reverse Full List            | Reverse Linked List (206)                   |
| Reverse Partial List         | Reverse Linked List II (92)                 |
| Reverse Second Half          | Palindrome (234), Reorder (143), Twin Sum (2130) |
| Two Pointers, Same Speed     | Intersection (160), Cycle II (142)          |
| Two Pointers, Different Speed| Cycle detection (141, 142), Find Middle     |
| Opposite Ends (with reverse) | Palindrome (234), Twin Sum (2130)           |
| Length-based Traversal       | Remove Nth from End (19)                    |

---

💡 **Tip:**  
Most medium LeetCode linked list problems are solved with:  
- **Find middle** + **Reverse half** + **Two pointers**  
This combo covers *Palindrome*, *Reorder List*, *Twin Sum*, and more.

# Definition for singly-linked list
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def template(self, head: ListNode) -> int:
        # -----------------------
        # 1. Find middle (fast/slow)
        # -----------------------
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Now `slow` is at the middle (start of 2nd half)

        # -----------------------
        # 2. Reverse the second half
        # -----------------------
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Now `prev` is the head of the reversed half

        # -----------------------
        # 3. Two pointers walk (left from head, right from reversed half)
        # -----------------------
        left, right = head, prev
        result = 0
        while right:   # usually run n/2 steps
            # Example operation: track max pair sum
            result = max(result, left.val + right.val)

            # Move both forward
            left = left.next
            right = right.next

        return result
```
