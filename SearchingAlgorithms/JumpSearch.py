"""
_ Jump Search: A searching algorithm for sorted array to check fewer elements by jumping ahead by
fixed steps or skipping some elements in place of searching all elements


For example
_ Suppose we have an array arr[] of size n and a block (to be jumped) of size m. Then we search in the
indexes arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]),
we perform a linear search operation from the index km to find the element x.
_ Let’s consider the following array:
    (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610).
The length of the array is 16. The Jump search will find the value of 55 with the following steps
assuming that the block size to be jumped is 4.
    STEP 1: Jump from index 0 to index 4;
    STEP 2: Jump from index 4 to index 8;
    STEP 3: Jump from index 8 to index 12;
    STEP 4: Since (the ele at index 12) > 55, we will jump back a step to come to index 8.
    STEP 5: Perform a linear search from index 8 to get the element 55.

How does it work:
+ Finding a specific value in a sorted arr by jumping through certain steps in the arr
+ The steps are determined by the sqrt of the length of the arr
    1. Determine the step size m by taking the sqrt of the length of the arr n
    2. Start the 1st ele of the arr and jump m steps until the value at that posn is greater
    than the target value. Once a value greater than the target is found, perform a linear
    search starting from the previous step until the target is founded or its clear that the
    target is not in the arr
    If the target is found, return the index. Otherwise, -1

"""

import math
def jumpSearch(array, key, n):
    # Finding block size to be jumped
    step = math.sqrt(n)

    # Finding the block where ele is present (if it is present)
    previous = 0
    while array[int(min(step, n) -1)] < key:
        previous = step
        step += math.sqrt(n)
        if previous >= n:
            return -1

    # Doing a linear search for x in block beginning with prev
    while array[int(previous)] < x:
        previous += 1

        # If we reached next block or end of arr, element is not present
        if previous == min(step, n):
            return -1

    # If element is found
    if array[int(previous)] == key:
        return previous

    return -1

# Driver code to test function
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)

    # Find the index of 'x' using Jump Search
    index = jumpSearch(arr, x, n)

    # Print the index where 'x' is located
    print("Number", x, "is at index", "%.0f" % index)
