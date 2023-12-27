"""
_ Binary Search: Is defined as searching algorithm used in a sorted array by repeatedly deviding the
search interval in half. The idea of binary search is to use the information that the array is sorted
and reduce the time complexity to O(log n)

Ex: Search 23
    2   5   8   12  16  23  38  56  70  90
Step 1:
-> Calculate the mid and compare the mid element with the key. If the key is less than mid element,
move to the left, otherwise move to the right as if the key is greater than the mid
-> Mid is 16
-> Left from 0 to 4, Right from 5 to 9
-> Key is larger than Mid (23 > 16) -> Move to the right and search that arr

Step 2: Right
    23  38  56  70  90
-> Calculate the mid = 56
-> Key is smaller than Mid (23 < 56) -> Move to the left and search that arr

Step 3: Left
    23  38
-> Key = Mid --> Done


How does it work?
+ Devide the search space into two halves by finding the middle index "Mid"
            Mid = (Left + Right) // 2
+ Compare the middle element of the search space with the key
+ If the key is founded in the middle element, the process is terminated
+ If the key is not founded in the middle element, choose which half will be used
as the next search space
    * If the key is smaller than the middle element, then the left side is used for next search
    * If the key is larger than the middle element, then the right side is used for next search
+ This process is continued until the key is founded or the total search space is exhausted

"""


# It returns location of x in given array arr
def binary_search(array, left, right, x):
    while left <= right:

        mid = (left + right) // 2

        # Check if x is present at mid
        if array[mid] == x:
            return mid

        # If x is greater, use right side
        elif array[mid] < x:
            left = mid + 1

        # If x is smaller, use left side
        else:
            right = mid - 1

    # If we reach here, then the element was not present
    return -1


def binary_search2(seq, item):
    begin = 0
    end = len(seq) - 1

    while begin <= end:
        mid = begin + (end - begin) // 2
        mid_value = seq[mid]
        if mid_value == item:
            return mid

        elif mid_value > item:
            end = mid - 1

        else:
            begin = mid + 1

    return None

# Main code
if __name__ == '__main__':
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 70, 90]
    key = 23

    # function call
    #res = binary_search(arr, 0, len(arr) - 1, key)
    res2 = binary_search2(arr, key)
    # Tip: Want to find the last index, we have to use the length of the array - 1
    # Because array starts at 0, not 1

    if res2 != -1:
        print("Element is present at index", res2)
    else:
        print("Element is not present in array")
