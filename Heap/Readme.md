# Heap Data Structure
#### Heap data structure is a complete binary tree that satisfies the heap property
- Max Heap: Any given node is always greater than its child nodes and the key of the root node is the largest among all other nodes.
```
         9
       /  \
      5    4
     / \   / 
    1  3  2
```

- Min Heap: Any given node is always smaller than its child nodes and the key of the root node 
is the smallest among all other nodes.
```
         1
       /  \
      2    3
     / \   / 
    4  5  9 
```
![](https://gochronicles.com/content/images/2021/08/heap-sort.gif)

### Operation:
- Heapify: The process of creating a heap data structure from a binary tree. It is used to create  a Min-Heap or a Max-Heap
```
    1. Initial array
        3   9   2   1   4   5

    2. Create a complete tree
            3
           /  \
          9    2
         / \   / 
        1  4  5

    3. Start from the first index of non-leaf node whose index is given by n/2 - 1
            3
          /  \
         9    2 ---> n/2 - 1
        / \   / 
        1  4  5

    4. Set the current element as target

    5. The index of left child is given by 2i + 1 and the right child is given by 2i + 2.
    If leftChild is greater than currentElement (i.e. element at ith index), set leftChildIndex as largest.
    If rightChild is greater than element in largest, set rightChildIndex as largest.

    6. Swap largest with currentElement
            3
          /  \
         9    5 
        / \   / 
        1  4  2

    7. Repeat step 3-7 until the subtrees are heapified
```
#### Psudocode
```
    Heapify(arr, size, i)
        set i as largest
        leftChild = 2i + 1
        rightChild = 2i + 2

        if leftChild > arr[largest]
            set leftChildIndex as largest
        if rightChild > arr[largest]
            set rightChildIndex as largest
        
        swap arr[i] and arr[largest]
    
    MaxHeap(arr, size):
        loop from first index of non-leaf node down to 0
            call Heapify function
    
    For MinHeap, both leftChild and rightChild must be larger than the parent for all nodes

```

## Insert Element to Heap
#### Psudocode
```
    If there is no node
        create newNode
    else (a node is already present)
        insert the newNode at the end (last node from left to right)
    heapify the array

1. Insert in the element at the end of the tree
        9
       /  \
      4     5
     / \   / \
    1  3  2  7 --> Inserted

2. Heapify the tree
        9
       /  \
      4     7
     / \   / \
    1  3  2   5

For MinHeap, the above algorithm is modified so that parentNode is always smaller than newNode.
```
##  Delete element from Heap
#### Psudocode
```    
    if nodeToBeDeleted is the leafNode
        remove the node
    else swap

1. Select the element to be deleted
        9
       /  \
  --> 3     7
     / \   / \
    1  4  2   5

2. Swap it with the last element.
        9
       /  \
  --> 5     7
     / \   / \
    1  4  2   3 <--

3. Remove the last element
        9
       /  \
      5     7
     / \   / \
    1  4  2   3 <-- Remove

4. Heapify the tree
        9
       /  \
      5     7
     / \   / 
    1  4  2 

For MinHeap, above algorithm is modified so that both childNodes are greater smaller than currentNode.
```
##  Peek (Find max/min)
- Peek returns the maximum element from MaxHeap or minimum element from MinHeap without deleting the node.

    ```For both MaxHeap and MinHeap --> return rootNode```


## Example
```
def heapify(arr, n, i):
    largest = i
    leftChild = 2*i + 1
    rightChild = 2*i + 2

    if leftChild < n and arr[i] < arr[leftChild]:
        largest = leftChild
    
    if rightChild < n and arr[i] < arr[rightChild]:
        largest = rightChild

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2) - 1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    
    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(num)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))


```