# BUBBLE SORT
'''
- Bubble Sort is a sorting algorithm that compares two adjacent elements and swaps
them until they are in intended order

<<<<<<< HEAD

How does it Work? (Ascending Order)
1. First Iteration(Compare and Swap)
    + Starting from the first index, compare the first and the second elements.
    + If the first element is greater than the second element, SWAP IT
    + Now, compare the second and the third elements. Swap them if they are not in order
    + The Sort will stop until process goes all with elements

2. Remaining Iteration
- The same process goes for the remaining iterations
- After iteration, the largest element among the unsorted elements is placed to the end
- In each iteration, the comparision takes place up to the last unsorted element.
- The array is sorted when all the unsorted elements are placed at their correct positions.

psudoCode: 
    def bubbleSort(arr):
        for i <- 1 to indexOflastElement - 1
            if left > right
                swap left, right
    end




'''
def bubbleSort(arr) -> str:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr



data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

'''
How does it Work? (Ascending Order)
1. First Iteration(Compare and Swap)
    + Starting from the first index, compare the first and the second elements.
    + If the first element is greater than the second element, SWAP IT
    + Now, compare the second and the third elements. Swap them if they are not in order
    + The Sort will stop until process goes all with elements

2. Remaining Iteration
- The same process goes for the remaining iterations
- After iteration, the largest element among the unsorted elements is placed to the end
- In each iteration, the comparision takes place up to the last unsorted element.
- The array is sorted when all the unsorted elements are placed at their correct positions.

psudoCode: 
    def bubbleSort(arr):
        for i <- 1 to indexOflastElement - 1
            if left > right
                swap left, right
    end


Complexity:
+ Best         --> O(n)
+ Worst        --> O(n^2)
+ Average      --> O(n^2)
+ Space Complexity --> O(1)
+ Stability    --> Yes


'''
# NORMAL
def bubbleSort(arr) -> str:
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# OPTIMIZED
def bubbleSort(arr) -> str:
    for i in range(len(arr)):
        swap = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        
        if not swap:
            return arr


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

