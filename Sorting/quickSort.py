# QUICK SORT
'''
- Like Merge Sort, this algorithm is also based on devide and conqueor paradigm,
but it uses this technique in a somewhat opposite manner, as all the hard work is
done before the recursive call.
- It picks an element has a pivot and partitions the given array around the picked
pivot by placing the pivot in its correct position in the sorted array

How does it work?
- The key process in quickSort is a partition(). The target of partitions is to place
the pivot (any element can be chosen to be a pivot) at its correct position in the 
sorted array and put all smallet elements to the left of the pivot, and all greater elements
in the right of pivot.
- Partition is done recursively on each side of the pivot after the pivot is placed in its
correct position and this finally sorts the array.

Complexity:
+ Best         --> O(n*log n)
+ Worst        --> O(n^2)
+ Average      --> O(n*log n) --> The fastest sorting Algorithm
+ Space Complexity --> O(1)
+ Stability    --> Yes


'''
def partition(array, start, end):
    # Choose the rightmost element as pivot
    pivot = array[end]

    # Pointer for preater element
    i = start - 1

    # Traverse through all elements and compare each element with pivot
    for j in range(start, end):
        if array[j] <= pivot:
            # If element <= pivot, swap it with the greater element pointed by i
            i = i + 1
            
            # Swapping element at i with element at j
            array[i], array[j] = array[j], array[i]
    
    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[end] = array[end], array[i + 1]

    # Return the position from where partition is done
    return i + 1

def quickSort(array, start, end):
    if start < end:
        ''' Find pivot element such that element smaller than pivot are 
        on the left and element greater than pivot are on the right '''
        pi =  partition(array, start, end)

        # Recursive call on the left of pivot
        quickSort(array, start, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, end)


if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)

    # Function call
    quickSort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")
