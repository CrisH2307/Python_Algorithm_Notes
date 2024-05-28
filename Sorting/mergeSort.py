# MERGE SORT
'''
- A sorting algorithm based on the principle Devide and Conquer
- The problem is divided into sub-problems. Each sub-problem is solved individually. 
Finally, sub-problems are combined to form the final solution

PsudoCode:
    def mergeSort(A, p, r):
        if p > r:
            return
        q = (p + r) / 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

Have we reached the end of any of the arrays?
    No:
        Compare current elements of both arrays 
        Copy smaller element into sorted array
        Move pointer of element containing smaller element
    Yes:
        Copy all remaining elements of non-empty array

'''
def mergeSort(arr):
    if len(arr) > 1:
        # r is the point where the array is divided into two subarrays
        r = len(arr) // 2
        L = arr[:r] # Slice notation [start : stop]
        M = arr[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        ''' until we reach either end of either L or M, pick larger among
        elements L and M and place them in the correct position at A[p..r] '''
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)