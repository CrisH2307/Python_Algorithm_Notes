# Print all subsets of a given set or array
'''
Given an array Arr[] of size N, print all the subsets of the array.
Subset: A subset of an array is a tuple that can be obtained from the
array by removing some (possibly all) elements of it

Input: N = 3, Arr = [1, 2, 3]
Output: {}
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



Explain:
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
    1 
    1 2 
    1 2 3 
    1 3 
    2 
    2 3 
    3     
    '''