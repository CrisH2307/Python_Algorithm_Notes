# Print all subsets of a given set or array
'''
Given an array Arr[] of size N, print all the subsets of the array.
Subset: A subset of an array is a tuple that can be obtained from the
array by removing some (possibly all) elements of it

Input: N = 3, Arr = [1, 2, 3]
Output: 
{}
{1}
{1, 2}
{1, 2, 3}
{1, 3}
{2}
{2, 3}
{3}
Explanation: These are all the subsets that can be formed from the given array,
it can be proven that no other subset exists other than the given output.


Input: N = 2, Arr = [2, 4]
Output: {}
{2}
{2, 4}
{4}
Explanation: These are all the subsets that can be formed from the given array, 
it can be proven that no other subset exists other than the given output.


Method 1: Using Backtracking
- Before jumping into the solution, can we observe some kind of relation between
the size of array N and number of subsets? Yes, there exists a relation
    N = 2 ^ N

- There is two options: Include or Exclude it
- Suppose and array of size 3 having {1, 2, 3}
Step by step:
- It starts with an empty subset and adds it to the result list
- It iterates through the elements of the input vector
    + Includes the current element in the subset
    + Recursive calls itself with the updated subset and the next index
    + Excludes the current element from the subset (backtracks)
'''
def calcSubset(A, res, subset, index):
    # Add the current subset to the result list
    res.append(subset[:])

    # Generate subsets by recursively including and excluding elements
    for i in range(index, len(A)):
        # Include the current element in the subset
        subset.append(A[i])

        # Recursively generate subsets with the current element included
        calcSubset(A, res, subset, i + 1)

        # Exclude the current element form the subset (Backtracking)
        subset.pop()

def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)
    return res



if __name__ == "__main__":
    array = [1, 2, 3]
    res = subsets(array)

    # Print the generated subsets
    for subset in res:
        print(*subset)
    '''
    Output:
    {}
    1 
    1 2 
    1 2 3 
    1 3 
    2 
    2 3 
    3     
    '''

'''
Method 2: Using Bit Manipulation
Observation: A bit can be either 0 or 1. What can we deduce from this?

Since, each element has only two choices i.e. either get included or get 
excluded. Assign these choices to a bit representation such that:
0 means Excluded
1 means Included
i'th bit represents i'th element of the array

Now lets say, there are N elements in the array. This array will have 2^N subsets. 
These subsets can be uniquely expressed in form of Bit representation of number from 0 to (2^N)-1.

Example: If elements in an array of size 2 = {A, B}
All the subsets of this array form the bit representation of number from 0 to (2^2)-1 i.e. 0 to 3

0 = 00 => A excluded, B excluded => { empty }
1 = 01 => A excluded, B included => { B }
2 = 10 => A included, B excluded => { A }
3 = 11 => A included, B included=> { A, B }


Step by step:
- Iterate numbers from 0 to (2^n) - 1
- Generate binary representation of that number and include the elements of array
as per below cases:
    + If the i'th bit is 1, the include i'th element of the array into current subset
    + If the i'th bit is 0, do nothing and continue
- Each bit representation of the number will give a unique subset.
'''
#Function to find the subsets of the given array
def findSubsets(nums, n):
    # Loop through all possible subsets using bit manipulation
    for i in range(1 << n):
        # Loop through all elements of the input array
        for j in range(n):
            # Check if the j'th bit is set in the current subset
            if i & (1 << j) != 0:
                # If the j'th bit is set, add the j'th element to the subset
                print(nums[j], end=" ")
        print()

arr = [1, 2, 3]
n = len(arr)
findSubsets(arr, n)