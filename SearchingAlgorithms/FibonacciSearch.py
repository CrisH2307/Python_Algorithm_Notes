"""
_ Fibonacci Search: A comparison based technique that uses Fibonacci numbers
to search an element in a sorted array


Given a sorted array arr[] of size n and an element x to be searched in it.
Return index of x if it is present in array else return -1.
Examples:

Input:  arr[] = {2, 3, 4, 10, 40}, x = 10
Output:  3
Element x is present at index 3.

Input:  arr[] = {2, 3, 4, 10, 40}, x = 11
Output:  -1
Element x is not present.

_ How does it work:
+ Find the smallest Fibonacci Number greater to n. Let it be fibM
+ Let the 2 Fibonacci Numbers preceding it be fibMm1 and fibMm2
[(m-1)’th Fibonacci Number]
[(m-2)’th Fibonacci Number]
+ While the arr has elements to be inspected
    1. Compare x with the last ele of the range covered by fibMm2
    2. If x matches, return index
    3. Else If x < element, move the three Fibonacci variables two Fibonacci down,
    indicating elimination of approximately rear two-third of the remaining arr.
    4. Else x > element, move the three Fibonacci variables one Fibonacci down.
    Reset offset to index. Together these indicate the elimination of approximately
    front one-third of the remaining arr.
+ Since there might be a single element remaining for comparison, check if fibMm1 is 1.
If Yes, compare x with that remaining element. If match, return index

"""


def fibonacci_search(array, key):
    n = len(array)
    if n == 0:
        return -1

    # Initialize Fibonacci Numbers
    fib1, fib2 = 0, 1
    fib3 = fib1 + fib2

    # Find the smallest Fi number greater than or equal to n
    while fib3 < n:
        fib1, fib2 = fib2, fib3
        fib3 = fib1 + fib2

    # Initialize variable variables for the current and prev split points
    offset = -1
    while fib3 > 1:
        i = min(offset + fib2, n - 1)

        # If x is greater than the value at index i, move the split point to the right
        if array[i] < key:
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2
            offset = i

        # If x is less than the value at index i, move the split point to the left
        elif array[i] > key:
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2
            offset = i

        else:
            return i

    # if x is not found in the arr, return -1
    if fib2 == 1 and array[offset + 1] == x:
        return offset + 1
    else:
        return -1


if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50,
           80, 82, 85, 90, 100, 235]
    n = len(arr)
    x = 235
    ind = fibonacci_search(arr, x)
    if ind >= 0:
        print("Found at index:", ind)
    else:
        print(x, "isn't present in the array");
