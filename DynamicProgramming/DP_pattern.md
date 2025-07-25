# Dynamic Programming Patterns and Concepts

This document aims to clarify different patterns of Dynamic Programming (DP) and when to use them. Understanding these patterns is crucial for solving optimization problems effectively.

## What is Dynamic Programming?

Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant computations. The two main approaches are:

1. **Top-Down (Memoization)**: Start from the main problem and break it down into subproblems, storing results
2. **Bottom-Up (Tabulation)**: Start from the smallest subproblems and build up to the main problem

### Key Concepts

1. **Optimal Substructure**
   - A problem has optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems
   - Example: In the shortest path problem, if node A is on the shortest path from B to C, then the shortest path from B to C is the shortest path from B to A plus the shortest path from A to C

2. **Overlapping Subproblems**
   - A problem has overlapping subproblems if the recursive solution contains many subproblems that are solved again and again
   - Example: In Fibonacci sequence, fib(5) = fib(4) + fib(3), and fib(4) = fib(3) + fib(2) - fib(3) is computed twice

3. **State Definition**
   - The state is the information needed to solve a particular subproblem
   - It should be minimal but sufficient to solve the problem
   - Example: In LIS, the state is dp[i] = length of LIS ending at index i

## Common DP Patterns with LeetCode Examples

### 1. 1D DP - Simple Sequences
- **Pattern**: `dp[i] = min/max(dp[i-1], dp[i-2], ...)`
- **Example Problems**:
  - [LeetCode 70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Fibonacci-like sequence
  - [LeetCode 198. House Robber](https://leetcode.com/problems/house-robber/) - Maximum sum with non-adjacent elements
  - [LeetCode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Kadane's algorithm
  - [LeetCode 509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) - Basic DP
  - [LeetCode 1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) - Extended sequence

#### Detailed Example 1: LeetCode 70. Climbing Stairs
```python
def climbStairs(n):
    # Top-Down with Memoization
    def dp(i):
        if i <= 1:
            return 1
        if i not in memo:
            memo[i] = dp(i-1) + dp(i-2)
        return memo[i]
    
    memo = {}
    return dp(n)

    # Bottom-Up with Tabulation
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

    # Space Optimized O(1) solution
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

**Key Points**:
- Simple state transition
- Linear time complexity
- Space optimization possible (O(1) space)
- Can be solved both recursively and iteratively
- Common pattern in sequence problems

#### Detailed Example 2: LeetCode 198. House Robber
```python
def rob(nums):
    # Top-Down with Memoization
    def dp(i):
        if i < 0:
            return 0
        if i not in memo:
            memo[i] = max(dp(i-1), nums[i] + dp(i-2))
        return memo[i]
    
    memo = {}
    return dp(len(nums) - 1)

    # Bottom-Up with Tabulation
    if not nums:
        return 0
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
    return dp[-1]

    # Space Optimized O(1) solution
    if not nums:
        return 0
    prev, curr = 0, nums[0]
    for num in nums[1:]:
        prev, curr = curr, max(curr, num + prev)
    return curr
```

**Key Points**:
- Non-adjacent elements constraint
- Two state transitions (take vs skip)
- Space optimization possible
- Common pattern in optimization problems

### 2. 2D DP - Grid Problems
- **Pattern**: `dp[i][j] = min/max(dp[i-1][j], dp[i][j-1], ...)`
- **Example Problems**:
  - [LeetCode 62. Unique Paths](https://leetcode.com/problems/unique-paths/) - Grid traversal
  - [LeetCode 64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) - Grid optimization
  - [LeetCode 72. Edit Distance](https://leetcode.com/problems/edit-distance/) - String transformation
  - [LeetCode 63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) - Grid with obstacles
  - [LeetCode 120. Triangle](https://leetcode.com/problems/triangle/) - Minimum path sum in triangle

#### Detailed Example 1: LeetCode 62. Unique Paths
```python
def uniquePaths(m, n):
    # Bottom-Up with Tabulation
    dp = [[0] * n for _ in range(m)]
    
    # Initialize first row and column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    # Fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

    # Space Optimized O(min(m,n)) solution
    if m > n:
        m, n = n, m
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    return dp[-1]
```

**Key Points**:
- Two-dimensional state space
- Multiple possible transitions
- Can be optimized with space (O(min(m,n)) space)
- Common pattern in grid traversal
- Initialization of boundaries is crucial

#### Detailed Example 2: LeetCode 72. Edit Distance
```python
def minDistance(word1, word2):
    # Bottom-Up with Tabulation
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the rest of the grid
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # delete
                    dp[i][j-1] + 1,    # insert
                    dp[i-1][j-1] + 1   # replace
                )
    
    return dp[m][n]

    # Space Optimized O(min(m,n)) solution
    if m > n:
        word1, word2 = word2, word1
        m, n = n, m
    
    dp = [0] * (n + 1)
    for j in range(n + 1):
        dp[j] = j
    
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i-1] == word2[j-1]:
                dp[j] = prev
            else:
                dp[j] = min(
                    prev + 1,
                    dp[j-1] + 1,
                    dp[j] + 1
                )
            prev = temp
    
    return dp[-1]
```

**Key Points**:
- Multiple state transitions (insert, delete, replace)
- Complex state management
- Space optimization possible
- Common pattern in string manipulation
- Initialization of boundaries is crucial

### 3. DP with Multiple States
- **Pattern**: `dp[i][state] = min/max(dp[i-1][prev_state], ...)`
- **Example Problems**:
  - [LeetCode 139. Word Break](https://leetcode.com/problems/word-break/) - String partitioning
  - [LeetCode 300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) - Sequence optimization
  - [LeetCode 416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) - Subset sum
  - [LeetCode 322. Coin Change](https://leetcode.com/problems/coin-change/) - Minimum coins
  - [LeetCode 494. Target Sum](https://leetcode.com/problems/target-sum/) - Expression evaluation

#### Detailed Example 1: LeetCode 300. Longest Increasing Subsequence
```python
def lengthOfLIS(nums):
    # Bottom-Up with Tabulation
    dp = [1] * len(nums)  # Initialize with minimum length 1
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

    # Optimized O(n log n) solution using binary search
    def lengthOfLIS(nums):
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
```

**Key Points**:
- Multiple states to consider
- More complex state transitions
- Often requires nested loops
- Can have optimized solutions
- Common pattern in sequence optimization

#### Detailed Example 2: LeetCode 416. Partition Equal Subset Sum
```python
def canPartition(nums):
    # Bottom-Up with Tabulation
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

    # Space Optimized solution
    def canPartition(nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        # Use bit manipulation
        possible = 1
        for num in nums:
            possible |= possible << num
        
        return (possible & (1 << target)) != 0
```

**Key Points**:
- Subset sum problem variation
- Bit manipulation optimization
- Space optimization
- Common pattern in subset problems
- Multiple solution approaches

### 4. DP with Bitmasking
- **Pattern**: `dp[mask] = min/max(dp[prev_mask], ...)`
- **Example Problems**:
  - [LeetCode 1982. Count Arrays That Are Distance Similar](https://leetcode.com/problems/count-arrays-that-are-distance-similar/) - Subset selection
  - [LeetCode 1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) - String combination
  - [LeetCode 1781. Sum of Beauty of All Substrings](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/) - Character counting
  - [LeetCode 1655. Distribute Repeating Integers](https://leetcode.com/problems/distribute-repeating-integers/) - Distribution problem
  - [LeetCode 1986. Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) - Task scheduling

#### Detailed Example 1: LeetCode 1239. Maximum Length of a Concatenated String with Unique Characters
```python
def maxLength(arr):
    def has_duplicates(s):
        return len(s) != len(set(s))
    
    # Filter out strings with duplicates
    arr = [s for s in arr if not has_duplicates(s)]
    
    # Bottom-Up with Bitmasking
    dp = [0] * (1 << len(arr))
    
    for mask in range(1, 1 << len(arr)):
        # Find the last set bit
        last = -1
        for j in range(len(arr)):
            if mask & (1 << j):
                last = j
        
        # Check if the current string can be added
        current_str = arr[last]
        if not has_duplicates(current_str + ''.join(arr[j] for j in range(len(arr)) if mask & (1 << j))):
            dp[mask] = dp[mask ^ (1 << last)] + len(current_str)
    
    return max(dp)

    # Optimized solution using bit manipulation
    def maxLength(arr):
        # Convert strings to bit masks
        masks = []
        for s in arr:
            mask = 0
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if mask & bit:  # duplicate character
                    break
                mask |= bit
            else:
                masks.append(mask)
        
        dp = [0] * (1 << len(masks))
        for mask in range(1, 1 << len(masks)):
            current_mask = 0
            for j in range(len(masks)):
                if mask & (1 << j):
                    if current_mask & masks[j]:  # duplicate character
                        dp[mask] = 0
                        break
                    current_mask |= masks[j]
            else:
                dp[mask] = bin(current_mask).count('1')
        
        return max(dp)
```

**Key Points**:
- Uses bit manipulation for state representation
- Can handle subsets efficiently
- Complex state transitions
- Often has exponential time complexity
- Common pattern in subset selection

### 5. DP on Trees
- **Pattern**: `dp[node] = min/max(dp[child1], dp[child2], ...)`
- **Example Problems**:
  - [LeetCode 337. House Robber III](https://leetcode.com/problems/house-robber-iii/) - Tree traversal
  - [LeetCode 124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) - Path optimization
  - [LeetCode 1245. Tree Diameter](https://leetcode.com/problems/tree-diameter/) - Tree diameter
  - [LeetCode 1377. Frog Position After T Seconds](https://leetcode.com/problems/frog-position-after-t-seconds/) - Tree probability
  - [LeetCode 1519. Number of Nodes in the Sub-Tree With the Same Label](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/) - Tree counting

#### Detailed Example: LeetCode 337. House Robber III
```python
def rob(root):
    def dp(node):
        if not node:
            return [0, 0]  # [not rob, rob]
            
        left = dp(node.left)
        right = dp(node.right)
        
        # If we rob this node, we cannot rob its children
        rob_this = node.val + left[0] + right[0]
        # If we don't rob this node, we take the max of robbing or not robbing its children
        not_rob_this = max(left[0], left[1]) + max(right[0], right[1])
        
        return [not_rob_this, rob_this]
    
    return max(dp(root))
```

**Key Points**:
- Multiple states per node
- Tree traversal with memoization
- Bottom-up approach through recursion
- Common pattern in tree problems
- State management is crucial

## Common DP Optimization Techniques

1. **Space Optimization**
   - Use rolling arrays
   - Store only necessary previous states
   - Example: Fibonacci sequence can be solved with O(1) space
   - Use bit manipulation for subset problems

2. **Memoization**
   - Store results of expensive function calls
   - Avoid redundant calculations
   - Use dictionaries or arrays for storage
   - Can be combined with other optimizations

3. **State Compression**
   - Reduce the number of states
   - Combine multiple dimensions
   - Use bit manipulation for state representation
   - Common in subset problems

4. **Binary Search**
   - Use when the problem has monotonic properties
   - Can reduce time complexity from O(n^2) to O(n log n)
   - Common in sequence problems

5. **Prefix/Suffix Arrays**
   - Precompute partial results
   - Can reduce time complexity
   - Common in array manipulation problems

## When to Use DP

1. **Optimization Problems**
   - Finding minimum/maximum values
   - Counting possibilities
   - Finding best paths
   - Subset selection
   - Tree traversal

2. **Overlapping Subproblems**
   - Same subproblems are solved multiple times
   - Results can be reused
   - Common in sequence and grid problems

3. **Optimal Substructure**
   - Solutions to subproblems can be combined
   - Larger problems can be solved using smaller solutions
   - Common in optimization problems

## Practice Tips

1. **Identify the State**
   - What information do you need to store?
   - What are the variables that change?
   - How can you minimize the state space?

2. **Define the Transition**
   - How do states relate to each other?
   - What are the possible moves?
   - Are there multiple choices?

3. **Base Cases**
   - What are the simplest cases?
   - What should be the initial values?
   - How do boundary conditions affect the solution?

4. **Optimize**
   - Can you reduce space complexity?
   - Are there redundant calculations?
   - Can you use bit manipulation?
   - Can you use binary search?

5. **Common Patterns to Recognize**
   - Sequence problems (Fibonacci, LIS)
   - Grid problems (Unique Paths, Edit Distance)
   - Subset problems (Subset Sum, Partition)
   - Tree problems (House Robber III, Maximum Path Sum)
   - String manipulation (Edit Distance, Word Break)

This document should help clarify the different patterns and when to use them. Practice is key to mastering DP - try implementing these patterns with different problems to solidify your understanding.
