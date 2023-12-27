"""
_ Sentinel Linear Search is the type of Linear Search where the number of comparisons is reduced as
compared to a traditional linear search.
_ In a normal Linear Search, only N comparisons are made.
_ In a Sentinel Linear Search, the sentinel value is used to avoid any out-of-bounds comparison.


How does it work?
+ The last ele of the array is replaced with the element to be searched and then the linear search
perform on the array without checking whether the current index is inside the index range of the
array or not because the element at be searched will definitely be found inside the array even if
it was not present in the original array sice the last element got replaced with it

_ Steps:
+ Initialize the search index variable i = 0
+ Set the last element of the array to the search key
+ While the search key is not equal ti tge current element of the arr (arr[i]), increment i
+ If i > size of arr or arr[i] == key, return i
+ Otherwise, the key is not presented in the arr, return None or -1

Input: arr[] = {10, 20, 180, 30, 60, 50, 110, 100, 70}, x = 180
Output: 180 is present at index 2
Input: arr[] = {10, 20, 180, 30, 60, 50, 110, 100, 70}, x = 90
Output: Not found

"""

"""
Given an array of n distinct integers and an element x. Search the element x in the array using minimum 
number of comparisons. Any sort of comparison will contribute 1 to the count of comparisons.
For example, the condition used to terminate a loop, will also contribute 1 to the count of comparisons 
each time it gets executed. Expressions like while (n) {n–;} also contribute to the count of comparisons 
as value of n is being compared internally so as to decide whether or not to terminate the loop. 
Examples: 
Input : arr[] = {4, 6, 1, 5, 8}, 
        x = 1
Output : Found

Input : arr[] = {10, 3, 12, 7, 2, 11, 9}, 
        x = 15
Output : Not Found

"""


def linear_search(arr, n, x):

    # 1st comparison
    if (arr[n -1] == x):
        return "Found"

    temp = arr[n-1]
    arr[n - 1] = x

    # No termination condition and thus no comparison
    i = 0

    while (i < n):
        # It will be executed at-most n times and therefore at-most n comparisons
        if arr[i] == x:
            # Replace arr[n - 1] with its actual element as in original 'arr[]'
            arr[n - 1] = temp

            # If x is founded before the (n - 1)th index, then it is present in the array final comparison
            if (i < n - 1):
                return "Found"

            # Else not present in the arr
            return "Not found"
        i = i + 1



def sentinel_linear_search(array, number, item):
    # Now we find the end element of the array
    end = array[n - 1]

    # The ele to be searched is placed at the last index
    arr[n - 1] = item
    i = 0

    while arr[i] != key:
        i += 1

    # Put the last ele at the back
    arr[n - 1] = end

    if (i < number - 1) or (arr[number - 1] == item):
        print(key, "is present at index", i)
    else:
        print("Not found")


# Main code
if __name__ == '__main__':
    arr = [10, 20, 180, 30, 60, 50, 110, 100, 70]
    n = len(arr)
    key = 180

    sentinel_linear_search(arr, n, key)
