# INSERTION SORT
'''
- Insertion sort is a sorting algorithm that places an unsorted element at its
suitable place in each iteration.
- It's similar as we sort cards in our hand in a card game.
- We assume that the first card is already sorted then, we select an unsorted card. 
If the unsorted card is greater than the card in hand, it is placed on the right 
otherwise, to the left. In the same way, other unsorted cards are taken and put in 
their right place.

How does it work?
1. The first element in the arr is assumed to be sorted. Take the second element
and store it separately in key. Compare key with the first element. If the first
element is greater than key, then key is placed in the front of the first element
2. Now the first two elements are sorted. Take the third element and compare it with
the elements on the left of it. Placed it just behind the element smaller than it. If
there is no element smaller than it, then place it at the beginning of the array.
3. Similarly, place every unsorted element at its correct position. 


PsudoCode:
    def insertionSort(arr)
        mark first element as sorted
        for each unsorted element X
            extract the element X
            for j <- lastSortedIndex down to 0
                if currentElement j > X
                    move sorted element to the right by 1
            break loop and insert X here
    end


Complexity:
+ Best         --> O(n)
+ Worst        --> O(n^2)
+ Average      --> O(n^2)
+ Space Complexity --> O(1)
+ Stability    --> Yes

'''
def insertionSort(arr):
    if len(arr) <=1 : return

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key




data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)