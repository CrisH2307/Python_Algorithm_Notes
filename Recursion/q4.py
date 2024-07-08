'''
Write a recursice function that takes two inputs n and m and outputs the number of unique paths
from the top left corner of a n x m grid.
Constraint: You can only move down or right 1 unit at a time


'''
def grid_paths(n,m):
    if n == 1 or m == 1:
        return 1
    return grid_paths(n, m - 1) + grid_paths(n - 1, m)
    


print(grid_paths(2,4))