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
