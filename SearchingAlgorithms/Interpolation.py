"""
_ Interpolation Search: Constructs new data points within the range of a discrete set of known
data points, where the values in a sorted arr are uniformly distributed. Oppositely Binary Search,
Interpolation may go to different locations according to the value of the key being searched
_ If key is closer to the last ele, it is likely to start search toward the end


How does it work?
+ In a loop, calculate the value of posn using the probe position formula
+ If its a match, return the index and exit
+ If the key < arr[posn], calculate the probe posn of the left sub-array. Otherwise, calculate right one
+ Repeat until a match is found or the sub-array reduces to 0

"""
def interpolation_Search(array, low, high, key):
    # Since the arr is sorted, an ele presents in arr must be in range defined by corner
    if (low <= high and key >= array[low] and key <= array[high]):

        # Probing the posn with keeping uniform distribution in mind
        posn = low + ((high - low) // (array[high] - array[low]) * ( key - array[low]))

        # Condition of target found
        if array[posn] == x:
            return posn

        # If x is larger, x is in right subarray
        if array[posn] < x:
            return interpolation_Search(array, posn + 1, high, key)

        # If x is larger, x is in right subarray
        if array[posn] > x:
            return interpolation_Search(array, low, posn - 1, key)

    return -1

def interpolationSearch(array, num, key):
    # Find the indexes of two corners
    low = 0
    high = (num - 1)

    # Since array is sorted, an ele present in array must be in range defined by corner
    while low <= high and key >= array[low] and key <= array[high]:
        if low == high:
            if array[low] == key:
                return low
            return -1

        # Probing the posn with keeping uniform distribution in mind
        posn = int(low + (((float(high - low) / (array[high] - array[low])) * (key - array[low]))))

        # founded
        if array[posn] == key:
            return posn

        # If x is larger, x is in upper part
        if arr[posn] < x:
            low = posn + 1

        # If x is smaller, x is in lower part
        else:
            high = posn - 1

    return -1


if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20,
           21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)

    # Element to be searched
    x = 18
    index = interpolation_Search(arr, 0, n - 1, x)
    index2 = interpolationSearch(arr, n, x)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")

    if index2 != -1:
        print("Element found at index", index2)
    else:
        print("Element not found")