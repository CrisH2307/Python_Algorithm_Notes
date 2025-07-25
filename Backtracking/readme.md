# Backtracking Algorithm
### What is Backtracking?
- Backtracking is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end.
- Its like trying different paths, and when you hit a dead end, you backtrack to the last choice and try a different route. 
- It is commonly used in situations where you need to explore multiple possibilities to solve a problem, like searching for a path in a maze or solving puzzles like Sudoku. When the dead end is reached, the algorithm backtracks to the previous decision point and explores a different path until a solution is found or all possibilities have been exhausted.

### Terminologies:
+ Candidate: A potential choice or element that can be added to the current solution
+ Solution: A valid and complete configuration that satifies all problem constraints.
+ Partial Solution: An intermediate or incomplete configuration being constructed during the backtracking process.
+ Decision Space: Set of all possible candidates or choices at each decision point.
+ Decision Point:Aspecific step in the algorithm where a candidate is chosen and added to the partial solution.
+ Feasible Solution: A partial or complete solution that address to all contraints.
+ Dead End: Occures when a partial solution cant be extended without violating constraints.
+ Backtrack: Involves undoing previous decisions and returning to a prior decision point.
+ Search Space: Includes all possible combinations of candidates and choices
+ Optimal Solution: Is the best possible solution.

### Types of Backtracking Problems:
+ Decision Problems: Here, we search for a feasible solution.
+ Optimization Problems: For this type, we search for the best solution.
+ Enumeration Problems: We find set of all possible feasible solutions to the problems of this type.

####  Recursion                      
+ Does not always need backtracking.    
+ Breaking them into smaller, similar subproblems and solving recursively             
+ Controlled by function calls and call stack
+ Ex: Tree, Graph Traversal, Merge Sort, Quick Sort, Binary Search

#### Backtracking
+ Uses recursion to solve problem
+ Solving problems with multiple choices and exploring options systematically, backtracking when needed        
+ Managed explicitly with loops and state      
+ Ex: Sudoku, Maze, Graph color, Knight Tour    

### How does it work?
By recursively exploring all possible solutions to a problem. It starts by choosing an intial position, and then it explores all possible extensions of that solution. If an extension leads to a solution, the algorithm returns that solution. If an extension does not lead to a solution, the algorithm backtracks to the prev solution and tries a different extension.

    1. Choose an initial solution
    2. Explore all possible extensions of the current solution
    3. If an extension leads to a solution, return that solution
    4. If an extension does not lead to a solution, backtrack to the previous solution and try a different extension.
    5. Repeat steps 2-4 until all possible solutions have been explored.

#### Ex: Finding the shortest path through a maze
A maze represented as a 2D array, where 0 represents an open space and 1 represents a wall.

#### Algorithm:

    1. Start at the starting point
    2. For each of the four possible directions (up, down, left, right)
    3. If moving in that direction leads to the ending point, return the path taken.
    4. If moving in that direction does not lead to the ending point, backtrack to the prev position and try a different direction.
    5. Repeat steps 2-4 until the ending point is reached or all possible paths have been explored.

Pseudocode for Backtracking:
```
    def solution(params):
        if (valid solution):
            store the solution
            return
        for (all choice):
            if(valid choice):
                apply(choice)
                solution(params)
                backtrack(remove choice)
        return

    Backtrack(x)
    if x is not a solution
        return false
    if x is a new solution
        add to list of solutions
    backtrack(expand x)
```
# Backtracking Patterns and Base Cases

This document aims to clarify the different patterns of backtracking and when to use which base cases. Understanding these patterns is crucial for solving problems effectively.

## Common Backtracking Patterns with LeetCode Examples

### 1. Subset/Combination Problems (for i in range(start))
- **Pattern**: `for i in range(start, len(nums))`
- **Base Case**: When the current path meets the required length or condition
- **Example**: 
  - [LeetCode 78. Subsets](https://leetcode.com/problems/subsets/) - All possible subsets
  - [LeetCode 77. Combinations](https://leetcode.com/problems/combinations/) - k-combinations
  - [LeetCode 39. Combination Sum](https://leetcode.com/problems/combination-sum/) - Target sum combinations
  - [LeetCode 216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) - k numbers sum to n
  - [LeetCode 40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) - Unique combinations with duplicates

#### Detailed Example 1: LeetCode 78. Subsets
```python
def subsets(nums):
    def backtrack(start):
        # Base case: every path is a valid subset
        result.append(current_subset.copy())
        
        for i in range(start, len(nums)):
            # Make choice
            current_subset.append(nums[i])
            
            # Explore further
            backtrack(i + 1)
            
            # Undo choice
            current_subset.pop()
    
    result = []
    current_subset = []
    backtrack(0)
    return result
```

**Key Points**:
- Uses `start` parameter to avoid duplicates
- Base case is implicit (every path is valid)
- Loop control acts as termination
- No need to check for termination since every path is valid

#### Detailed Example 2: LeetCode 77. Combinations
```python
def combine(n, k):
    def backtrack(start):
        # Base case: when we have k numbers
        if len(current_combination) == k:
            result.append(current_combination.copy())
            return
            
        for i in range(start, n + 1):
            # Make choice
            current_combination.append(i)
            
            # Explore further
            backtrack(i + 1)
            
            # Undo choice
            current_combination.pop()
    
    result = []
    current_combination = []
    backtrack(1)
    return result
```

**Key Points**:
- Explicit base case when length == k
- Uses start parameter to avoid duplicates
- Similar to subsets but with length constraint

### 2. Permutation Problems (for i in range(len(nums))
- **Pattern**: `for i in range(len(nums))`
- **Base Case**: When all elements have been used
- **Example**: 
  - [LeetCode 46. Permutations](https://leetcode.com/problems/permutations/) - All permutations
  - [LeetCode 47. Permutations II](https://leetcode.com/problems/permutations-ii/) - Permutations with duplicates
  - [LeetCode 31. Next Permutation](https://leetcode.com/problems/next-permutation/) - Lexicographical order
  - [LeetCode 60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) - kth permutation
  - [LeetCode 90. Subsets II](https://leetcode.com/problems/subsets-ii/) - Subsets with duplicates

#### Detailed Example 1: LeetCode 46. Permutations
```python
def permute(nums):
    def backtrack():
        # Base case: when all elements are used
        if len(current_permutation) == len(nums):
            result.append(current_permutation.copy())
            return
            
        for i in range(len(nums)):
            if not used[i]:
                # Make choice
                current_permutation.append(nums[i])
                used[i] = True
                
                # Explore further
                backtrack()
                
                # Undo choice
                used[i] = False
                current_permutation.pop()
    
    result = []
    current_permutation = []
    used = [False] * len(nums)
    backtrack()
    return result
```

**Key Points**:
- Uses `used` array to track elements
- Base case is explicit (all elements used)
- Requires undoing choices
- Each element can appear only once

#### Detailed Example 2: LeetCode 47. Permutations II (with duplicates)
```python
def permuteUnique(nums):
    def backtrack():
        # Base case: when all elements are used
        if len(current_permutation) == len(nums):
            result.append(current_permutation.copy())
            return
            
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
                
            # Make choice
            current_permutation.append(nums[i])
            used[i] = True
            
            # Explore further
            backtrack()
            
            # Undo choice
            used[i] = False
            current_permutation.pop()
    
    result = []
    current_permutation = []
    used = [False] * len(nums)
    nums.sort()  # Sort to handle duplicates
    backtrack()
    return result
```

**Key Points**:
- Handles duplicates by sorting and skipping identical elements
- Uses both `used` array and previous element check
- More complex base case handling
- Requires careful state management

### 3. No Loop Backtracking
- **Pattern**: Direct recursive calls without loops
- **Base Case**: When the current state meets the termination condition
- **Example**: 
  - [LeetCode 51. N-Queens](https://leetcode.com/problems/n-queens/) - Place n queens
  - [LeetCode 37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) - Solve Sudoku
  - [LeetCode 93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) - Valid IP addresses
  - [LeetCode 131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) - Palindrome partitions
  - [LeetCode 140. Word Break II](https://leetcode.com/problems/word-break-ii/) - Sentence reconstruction

#### Detailed Example 1: LeetCode 51. N-Queens
```python
def solveNQueens(n):
    def backtrack(row):
        # Base case: when all queens are placed
        if row == n:
            result.append([''.join(row) for row in board])
            return
            
        for col in range(n):
            if is_valid(row, col):
                # Make choice
                board[row][col] = 'Q'
                
                # Explore further
                backtrack(row + 1)
                
                # Undo choice
                board[row][col] = '.'
    
    def is_valid(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
                
        # Check diagonals
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
            
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
            
        return True
    
    result = []
    board = [['.'] * n for _ in range(n)]
    backtrack(0)
    return result
```

**Key Points**:
- Uses explicit validity checks
- Base case is when all rows are placed
- No loop needed - each recursive call represents a row
- Complex state management with board representation

#### Detailed Example 2: LeetCode 131. Palindrome Partitioning
```python
def partition(s):
    def backtrack(start):
        # Base case: when we reach the end of the string
        if start == len(s):
            result.append(current_partition.copy())
            return
            
        for end in range(start + 1, len(s) + 1):
            # Check if the substring is palindrome
            if s[start:end] == s[start:end][::-1]:
                # Make choice
                current_partition.append(s[start:end])
                
                # Explore further
                backtrack(end)
                
                # Undo choice
                current_partition.pop()
    
    result = []
    current_partition = []
    backtrack(0)
    return result
```

**Key Points**:
- Uses string slicing for partitions
- Base case is when we reach the end of string
- No need for explicit used array
- Each recursive call represents a new partition point

## When You Don't Need Base Cases

1. **When the Problem Space is Bounded**:
   - If the problem naturally terminates (e.g., reaching end of array)
   - If the recursive calls will naturally stop (e.g., reaching invalid state)

2. **When Using Loop Control**:
   - The loop itself acts as a natural termination
   - Example: `for i in range(len(nums))` naturally stops when i reaches len(nums)

3. **When Using Validity Checks**:
   - If you have checks that prevent invalid states
   - Example: In N-Queens, if you check if a position is valid before placing

## Example Patterns

### Pattern 1: Subset/Combination
```python
def backtrack(start):
    # Base case: when we've reached the desired length or condition
    if condition_met():
        result.append(current_path.copy())
        return
    
    for i in range(start, len(nums)):
        # Make choice
        current_path.append(nums[i])
        
        # Explore further
        backtrack(i + 1)
        
        # Undo choice
        current_path.pop()
```

### Pattern 2: Permutation
```python
def backtrack():
    # Base case: when all elements are used
    if len(current_path) == len(nums):
        result.append(current_path.copy())
        return
    
    for i in range(len(nums)):
        if not used[i]:
            # Make choice
            current_path.append(nums[i])
            used[i] = True
            
            # Explore further
            backtrack()
            
            # Undo choice
            used[i] = False
            current_path.pop()
```

### Pattern 3: No Loop Backtracking
```python
def backtrack(row):
    # Base case: when all rows are placed
    if row == n:
        result.append(current_board.copy())
        return
    
    for col in range(n):
        if is_valid(row, col):
            # Make choice
            place_queen(row, col)
            
            # Explore further
            backtrack(row + 1)
            
            # Undo choice
            remove_queen(row, col)
```

## Key Takeaways

1. **Base cases are essential** when you need to explicitly stop recursion
2. **Loop control** can act as implicit base cases
3. **Validity checks** can prevent unnecessary recursion
4. **Start parameter** controls the exploration space
5. **Path tracking** is crucial for maintaining state

## Practice Tips

1. Always start with a clear understanding of the problem space
2. Identify what constitutes a valid solution
3. Determine the natural termination points
4. Consider what choices need to be made at each step
5. Think about how to undo choices (backtrack)

This document should help clarify the different patterns and when to use which approach. Remember that practice is key to mastering backtracking - try implementing these patterns with different problems to solidify your understanding.
