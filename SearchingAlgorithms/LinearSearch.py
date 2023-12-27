"""
_ Linear Search is defined as a sequential search algorithm that starts at one
end and goes through each element of a list until the desired element is found,
otherwise the search continues till the end of the data set.
_ It is defined as the searching algorithm there the list or data set is traversed

How does it work?
+ Every ele is considered as a potential match for the key and checked for the same
+ If any element is found equal to the key, the search is sucessful and the
index of that element is returned
+ If no element is found equal to the key, the search is yields "No match found"

Find '20'
    10  50  40  43  32  30  20
"""

def linear_search(arr, length, key):
    for i in range(length):
        if (arr[i] == key):
            return i
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [10, 50, 30, 70, 80, 20, 90, 40]
    key = 30
    length = len(arr)

    # function call
    result = linear_search(arr, length, key)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)