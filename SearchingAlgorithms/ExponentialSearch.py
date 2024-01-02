"""
_ Exponential Search: Finding posn by locating an element by narrowing down the search
range in a series of steps that grow exponentially.


Given a sorted array, and an element x to be
searched, find position of x in the array.

Input:  arr[] = {10, 20, 40, 45, 55}
        x = 45
Output: Element found at index 3

Input:  arr[] = {10, 15, 25, 45, 55}
        x = 15
Output: Element found at index 1

How does it work?
+ Start with sub-arr size 1 and compare its last element with x, then try size 2 then 4
and so on until last element of a sub-arr is not greater
"""


def exponential_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1

    # Find range for binary search by repeatedly doubling i
    i = 1
    while i < n and arr[i] < x:
        i *= 2

    # Perform binary search on the range [i/2, min(i, n-1)]
    left = i // 2
    right = min(i, n - 1)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # Driver Code
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 10
    result = exponential_search(arr, x)
    if result == -1:
        print("Element not found in the array")
    else:
        print("Element is present at index %d" % (result))
