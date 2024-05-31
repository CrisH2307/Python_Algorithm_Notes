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

Complexity:
+ Best         --> O(n*log n)
+ Worst        --> O(n*log n)
+ Average      --> O(n*log n)
+ Space Complexity --> O(n)
+ Stability    --> Yes


'''
# def mergeSort(arr):
#     if len(arr) > 1:
#         # r is the point where the array is divided into two subarrays
#         r = len(arr) // 2
#         L = arr[:r] # Slice notation [start : stop]
#         M = arr[r:]

#         # Sort the two halves
#         mergeSort(L)
#         mergeSort(M)

#         i = j = k = 0

#         ''' until we reach either end of either L or M, pick larger among
#         elements L and M and place them in the correct position at A[p..r] '''
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = M[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
        
#         while j < len(M):
#             arr[k] = M[j]
#             j += 1
#             k += 1

def mergeSort(arr) -> None:
    if len(arr) > 1:
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]


        # recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

        # merge
        i = 0    # Keep track the leftmost of the array
        j = 0    # Keep track the rightmost of the array
        k = 0    # Keep track the merged array

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

            
# # Print the array
# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()


# Driver program
if __name__ == '__main__':
    nums = [2,3,5,6,1,4,9,12,40,33,23]
    mergeSort(nums)
    print(nums)
