"""
_ Meta Binary Search / One-Sided Binary Search: Is a modified form of binary search that incrementally
constructs the index of the target value in the array.

Here is the pseudocode for Meta Binary Search:
function meta_binary_search(A, target):
    n = length(A)
    interval_size = n
    while interval_size > 0:
        index = min(n - 1, interval_size / 2)
        mid = A[index]
        if mid == target:
            return index
        elif mid < target:
            interval_size = (n - index) / 2
        else:
            interval_size = index / 2
    return -1

Input: [-10, -5, 4, 6, 8, 10, 11], key_to_search = 10
Output: 5

Input: [-2, 10, 100, 250, 32315], key_to_search = -2
Output: 0

How does it work?
+ Store number of bits to represent the largest arr index in variable lgArr
+ Use lgArr to start off the search in a for loop
+ If the ele is found, return posn
+ Otherwise, incrementally construct an index to reach the target value in the for loop
+ If ele is found return posn, otherwise -1

"""
import math


def meta_binary_search(arr, key):
    n = len(arr)

    # Set the number of bits to represent
    lgArr = int(math.log2(n - 1) + 1)

    posn = 0
    for i in range(lgArr - 1, -1, -1):
        if (A[posn] == key):
            return posn
        # Now incrementally construct the index of the target value
        new_posn = posn | (1 << i)

        # Find the element in one direction and update posn
        if (new_posn < n) and (arr[new_posn] <= key):
            posn = new_posn

    # If ele is founded, return it. Otherwise, -1
    if (A[posn] == key):
        return posn
    else:
        return -1


# Driver code
if __name__ == "__main__":
    A = [-2, 10, 100, 250, 32315]
    print(meta_binary_search(A, 100))
