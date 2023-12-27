"""
_ Ternary Search: Used to find the position of a target value within a sorted arr.
It operates on the principle of dividing the arr into 3 parts instead of 2. To
narrow down the search space by comparing the target value with elements at 2 points
that divide the arr into 3 equal parts
    mid1 = left + (right - left) / 3
    mid2 = right – (right - left) / 3

How does it work?
1. Initialization
    + Begin with a sorted arr
    + Set 2 ptrs, left and right, initially pointing to the first and last elements of the arr

2. Divide the arr
    + Calculate two midpoints, mid1 and mid2, dividing the current search space into 3
    roughly equal parts:
        mid1 = left + (right - left) / 3
        mid2 = right – (right - left) / 3
    + The arr is now effectively divided into [left, mid1], (mid1, mid2), and [mid2, right]

3. Comparison with Target
    + If target = element at mid1 or mid2, the search is successful and the index is returned
    + If target < element mid1, update right pointer to mid1 - 1
    + If target > element mid2, update left pointer to mid2 + 1
    + If target is between mid1 and mid2, update left to mid + 1, right to mid2 - 1

4. Repeat or Conclude
    + Repeat the process with the reduced search space until the target is found or
    the search space becomes empty
    + If the search space is empty and the target is not found. Return the value
    indicating that the target is not present in the array

"""
# Function to perform Ternary Search


def ternarySearch(l, r, key, ar):
    while r >= l:

        # Find mid1 and mid2
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        # Check if key is at any mid
        if key == ar[mid1]:
            return mid1
        if key == ar[mid2]:
            return mid2

        # Since key is not present at mid,
        # Check in which region it is present
        # Then repeat the search operation in that region
        if key < ar[mid1]:
            # key lies between l and mid1
            r = mid1 - 1
        elif key > ar[mid2]:
            # key lies between mid2 and r
            l = mid2 + 1
        else:
            # key lies between mid1 and mid2
            l = mid1 + 1
            r = mid2 - 1

    # key not found
    return -1


# Driver code

# Get the list
# Sort the list if not sorted
ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Starting index
l = 0

# end element index
r = 9

# Checking for 5
# Key to be searched in the list
key = 5

# Search the key using ternary search
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# Checking for 50
# Key to be searched in the list
key = 50

# Search the key using ternary search
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)