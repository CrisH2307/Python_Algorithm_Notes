# Tower of Hanoi
'''
Problem statement
- You are given three rods (numbered 1 to 3), and ‘N’ disks initially placed on the first rod, 
one on top of each other in increasing order of size ( the largest disk is at the bottom). 
You are supposed to move the ‘N’ disks to another rod(either rod 2 or rod 3) using the following rules 
and in less than 2 ^ (N) moves.
    1. You can only move one disk in one move. 
    2. You can not place a larger disk on top of a smaller disk.
    3. You can only move the disk at the top of any rod.    

Note:
- You may assume that initially, the size of the ‘i’th disk from the top of the stack is equal to ‘i’, i.e. 
the disk at the bottom has size ‘N’, the disk above that has size ‘N - 1’, and so on. The disk at the top 
has size 1.

Sample Input 1 :
2
1
2

Sample Output 1 :
1
1

Explanation of Sample Input 1 :
In the first test case, 
you can move the only disk to either rod 2 or rod 3. The matrix to be returned should be either 
{ { 1, 2 } } or { {1, 3 } }.
In the second test case, 
you can move the topmost disk from rod 1 to rod 2. Then move the remaining disk from rod1 to rod 3. 
Now move the disk in rod 2 to rod 3. . One of the correct ways to return the output is 
{ { 1, 2 }, { 1, 3 }, { 2, 3 } }.  

Sample Input 2 :
1
3

Sample Output 2 :
1

Explanation of Sample Input 2 :
One of the correct matrices is 
{ { 1, 2 }, { 1, 3 }, { 2, 3 }, { 1, 2 }, { 3, 1 }, { 3, 2 }, { 1, 2 } }.

'''
def towerOfHanoi(n):
    # Return a 2-D array
    def solve(n, source, destination, auxiliary, result):
        if n == 1:
            result.append([source, destination])
            return
        solve(n-1, source, auxiliary, destination, result)
        result.append([source, destination])
        solve(n-1, auxiliary, destination, source, result)

    result = []
    solve(n, 1, 3, 2, result)
    return result

print(towerOfHanoi(1))  # Output: [[1, 3]]
print(towerOfHanoi(2))  # Output: [[1, 2], [1, 3], [2, 3]]
print(towerOfHanoi(3))  # Output: [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]