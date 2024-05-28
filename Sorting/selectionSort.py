# SELECTION SORT
'''
- Selection Sort is a sorting algorithm that selects the smallest element from an unsorted
list in each iteration and places that element at the beginning of the unsorted list.

How does it work?
1. Set the first element as minimum.
2. Compare minimun with the second element. If the second element is smaller than minimum,
assign the second element as minimum. Compare minimun with the third element. Again, if the
third element is smaller, then assign minimum to the third element, otherwise do NOTHING. The
process goes on until the last element
3. After each iteration, minimun is placed in the frong of the unordered list
4. For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated
until all the elements are placed at their correct positions.

PsudoCode:
    def selectionSort(arr)
        repeat (sizeofArr - 1) times
        set the first unsorted element as the minimun
        for each of the unsorted elements
            if element < currentMin
                set element as newMinimum
        swap minimun with first unsorted position
    end selectionSort

Complexity:
+ Best         --> O(n^2)
+ Worst        --> O(n^2)
+ Average      --> O(n^2)
+ Space Complexity --> O(1)
+ Stability    --> No


'''

def selectionSort(arr):
    size = len(arr)
    currentMin = arr[0]
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


data = [-2, 45, 0, 11, -9]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)