# EXAMPLE 1: Printing all solutions in N-Queen Problem:
''' 
The N Queen is the problem of placing N chess queens on an NxN chessboard so that no two queens 
attack each other.
Task: To print all solutions in N-Queen. Each solution contains distinct board configurations of
the N-queens' placement, where the solutions are a Permunation of [1,2,3,..n] increasing order.

Explaination:
- Idea is to place queens one by one in different columns, starting from the leftmost column.
When we place a queen in a column, we check for clashes with already placed queens. In the 
current column, if we find a row for which there is no clash, we mark this row and column as part
of the solution. If we dont find suck a row due to clashes then we backtrack and return false.
1. Start in the leftmost column
2. If all queens are placed --> return True
3. Try all rows in the current column. Do following for every tried row.
    + If the queen can be placed safely in this row -> Mark this [row, col] as part
    of solution and recursively check if placing queen here leads to a solution.
    + If placing queen in [row, col] leads to a solution -> return True
    + If placing queen doesn't lead to a solution -> Remove this [row, col] / Backtrack 
    and go back to step a to try other rows.
4. If all rows have been tried and nothing worked, return false to trigger backtracking.

- Whether we have a previously placed queen in a column or in left diagonal or in 
right diagonal in O(1) time. We can observe that:
    + For all cells in a particular left diagonal, their row + col = constant
    + For all cells in a particular right diagonal, their row - col + n - 1 = constant
- Let say we placed a queen at [2,0] 
-> [2,0] have leftDiagonal value = 2. Now we can't place another queen at [1,1] and [0,2]
because both of these have same leftDiagonal value as [2,0]. Similar thing can be noticed
for the right diagonal as well
'''

result = []

# A utility function to print solution
'''
A ultility funtion to check if a queen can be placed on board[row][col]. Note that this 
function is called when 'col' queens are already placed in columns from 0 to col -1.
We need to check only left side for attacking queens.
'''
def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False
        
    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check lower diagonal on the left side
    i, j = row, col
    while j >= 0 and i < len(board):
        if board[i][j]:
            return False
        i, j = i + 1, j - 1
    
    return True

# Make a recursive utility function to solve N Queen problem
def solveNQUtil(board, col):
    # Base case: If all queens are placed -> return True
    if col == len(board):
        place = []
        for i in board:
            for j in range(len(i)):
                if i[j] == 1:
                    place.append(j + 1)
        result.append(place)
        return True
    
    # Consider this col and try placing this queen in all rows one by one
    res = False
    for i in range(len(board)):
        # Check if queen can be placed on board[i][col]
        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # Make res True if any placement is possible
            res = solveNQUtil(board, col + 1) or res 

            ''' If placing queen in board[i][col] doesnt lead to a solution, 
            then remove queen from board[i][col] '''
            board[i][col] = 0       # --> THIS IS BACKTRACKING
    
    # If queen can't be place in any row in this column col then return False
    return res

''' This function solves the N Queen problem using Backtracking. It mainly uses solveNQUtil() 
to solve the problem. It returns false if queens cannot be placed, otherwise return true and 
prints placement of queens in the form of 1s. There may be more than one solutions, 
this function prints one of the feasible solutions.'''
def solveNQ(n):
    result.clear()
    board = [[0 for j in range(n)] for i in range (n)]
    solveNQUtil(board, 0)
    result.sort()
    return result

n = 9
res = solveNQ(n)
print(res)

# [ 2 4 1 3 ][ 3 1 4 2 ]