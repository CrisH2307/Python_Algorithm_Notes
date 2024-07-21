# PRIORITY QUEUE
'''
- A special type of queue in which each element is associated with a priority value.
- Elements are served on the basis of their priority. That is higher priority elements are served first
- However, if elements with the same priority occur, they are served according to their order in the queue.

Assigning priortiy queue:
- The value of the element itself is considered for assigning the priority.
Ex: The element with the highest value is considered the highest priority element. However, in other cases, 
we can assume the element with the lowest value as the highest priority element.

Difference between Priority Queue and Normal Queue
- In a queue, the first-in-first-out rule is implemented whereas, in a priority queue, the values are 
removed on the basis of priority. The element with the highest priority is removed first.

1. Inserting an Element into the Priority Queue
+ Insert the new element at the end of the tree. 
+ Heapify the tree. 
    If there is no node, 
        create a newNode.
    else (a node is already present)
        insert the newNode at the end (last node from left to right.
  
    heapify the array

2. Deleting an Element from the Priority Queue
+ Select the element to be deleted.
+ Swap it with the last element. 
+ Remove the last element. 
+ Heapify the tree. 
    If nodeToBeDeleted is the leafNode
        remove the node
    Else swap nodeToBeDeleted with the lastLeafNode
        remove noteToBeDeleted
    heapify the array

3. Peeking from the Priority Queue (Find max/min)
- For both Max heap and Min Heap
    return rootNode


'''

# # Function to heapify the tree
# def heapify(arr, n, i):
#     # Find the largest among root, left child and right child
#     largest = i
#     left = 2*i + 1
#     right = 2*i + 2

#     if left < n and arr[i] < arr[left]:
#         largest = left
    
#     if right < n and arr[largest] < arr[right]:
#         largest = right
    
#     # Swap and continue heapifying if root is not the largest
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)

# # Function to insert an element into the tree
# def insert(array, num):
#     size = len(array)
#     i = 0
#     for i in range(0, size):
#         if num == array[i]:
#             break
#     array[i], array[size - 1]= array[size - 1], array[i]
#     array.remove(size - 1)

#     for i in range((len(array) // 2) - 1, -1, -1):
#         heapify(array, len(array), i)


# arr = []

# insert(arr, 3)
# insert(arr, 4)
# insert(arr, 9)
# insert(arr, 5)
# insert(arr, 2)

# print ("Max-Heap array: " + str(arr))

# deleteNode(arr, 4)
# print("After deleting an element: " + str(arr))
import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return not self.elements
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)

if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # Item, priority
    pq.put("eat", 2)
    pq.put("code", 1)
    pq.put("sleep", 3)

    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())

