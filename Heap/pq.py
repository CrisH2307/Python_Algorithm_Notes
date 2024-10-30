'''
Priority Queues: Everything in queue has a priority and the highest priority item is removed
(as opposed to oldest item)

push(data) - add data to priority queue

pop() - removes highest priority item from priority queue

front() - returns highest priority item in the priority queue

Methods for implementing P.Q
1. Sorted Array: Sorted by priority, put highest priority item at the back of the array
    push(data) - O(n), we need to find the place to put it and put it in (which involves moving the items over),
                 we can binary search so make easier, however if the array is small, it is not neccesary the fastest,
                 even if binary search is fast, the insertion still O(n) cuz shift everything after it to the back (move over).
    pop() - O(1)
    front() - O(1)

2. Sorted Linked List: Sorted by priority, put the highest priority item at the front of the linked list
    push(data) - O(n), finding where to put the new node is O(n), it has to traverse the list. Actual intersion is O(1),
                 total cost is still O(n) beacause sometimes it has to traverse at the end of the list
    pop() - O(1) - popfront
    front() - O(1)

3. Unsorted Array: 
    push(data) - O(1), add the back of the array
    pop() - O(n) - to find the highest priority item and then shift other numbers to remove
    front() - O(n) - to find the highest priority item, look for entire list

-- BEST SOLUTION
This course will talk only binary heaps so when we talk about heaps its always binary heap
4. Binary Heap: Complete binary tree (shape of the data structure) where the heap order property is maintained.
    push(data) - O(log n)
    pop() - O(log n) 
    front() - O(1)

- Trees: Data structure where nodes are linked together through parent child relationship
- Binary Trees: Trees where each node can have most two children
- Completed Binary Tree: Are binary trees where every node at one level must exist before
any nodes can be added to the next level and node have to added from left to right
- Heap Order Property: parent has higher priority than child
    + Min-heap: Smaller value higher priority


Inserting into a binary heap:
- Remember binary heap must be complete binary tree where heap order property is maintained
- Create an empty node such that the tree is still a complete binary tree
    + If value can be placed into empty spot without violating the heap order property put it in
    + Otherwise pull parent value into empty spot making parent the empty spot
    + Repeat these steps until value is placed
=> Empty spot can only move log n times. It's only to move parent nodes without touching others node
and we dont check siblings or cousin nodes, only check parent with straight moving up ==> O(log n)
 

Removing from a binary heap:
- Again.. want to maintain complete binary tree and heap order
- Value that is popped off is at the root (highest priority)
- But.. node that is removed is bottom right most.. for completeness
- This mean value that was in bottom right most node needs a new home
- Algorithm:
    + Store bottom right most node's value into a temp
    + Delete bottom right most node
    + Empty out the root
        + Try to put bottom right most node's value into empty spot.
        + If it can't be placed there without breaking heap order, pull up higher priority child
        and making that node empty
        + Repeat until value is placed (worst case would be a leaf node)
==> O(log n), empty the root node, continously find the place can store, but not nescessary to traverse all node


Heap Implementation:
- Heaps are implemented using just an array
- Root of a heap is stored at array[0]
- For any given node where the data is stored at index idx:
    Left child is at: idx * 2 + 1
    Right child is at: idx * 2 + 2
    Parent (for non-root node): (idx - 1) // 2


How to create a heap from an array in-place
- Make heap by applying heapify over and over
- Any leaf node is a heap
==> O(n)


Heap Sort
- Heap Sort is a based on building and dismantling a heap
- Heap remove values based on priority - Sorted order (by priority)
- Cost to build a heap is O(n) using the inplace makeheap algorithm
- Cost to dismantle the heap is O(n log n) by performing n removes each of which costs O(log n)

To sort from smallest to biggest we must build and dismantle a Maxheap (higher values have higher priority)

'''

class 