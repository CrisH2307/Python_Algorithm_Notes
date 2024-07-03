# Devide and Conquer Algorithm

### What is Devide and Conquer?
#### A strategy of solving a large problem by:
+ Breaking the problem into smaller sub-problems
+ Solving the sub-problems, and combining them to get the disired output

![](https://miro.medium.com/v2/resize:fit:1150/1*xjYT0Y3FT_K-xFEP-q_k_Q.gif)


### How does it work??
    1. Divide: Divide the given problem into sub-problems using recursion.
    2. Conquer: Solve the smaller sub-problems recursively. If the subproblem is small enough, then solve it directly.
    3. Combine: Combine the solutions of the sub-problems that are part of the recursive process to solve the actual problem

### Ex: Merge Sort
    1. Let the given array be: 
        7   6   1   5   4   3

    2. Divide the array into two halves. 
        7   6   1        5   4   3

    3. Again, divide each subpart recursively into two halves until you get individual elements. 

    4. Combine the individual elements in a sorted manner. Here, conquer and combine steps go side by side. 

        1   6   7       3   4   5


    =>  1   3   4       5   6   7


### Time Complexity 
+ O(nlogn)
