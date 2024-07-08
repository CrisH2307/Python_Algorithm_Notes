'''
Write a function that counts the number of ways you can partition n objs using parts up to m (assuming m >= 0)


Explain:
1. Make the simple output
    partition(0, 0) -> 1
    partition(0, 1) -> 1
    partition(0, 2) -> 1
    => Base case will be 1 if n = 0

    partition(1, 0) -> 0
    partition(2, 0) -> 0
    => Base case will be 0 if m = 0

2. Visualize the problem
- As we can see all problems in larger problem are repeated in smaller problem
Ex: partition(7, 4) will have same problem in partition(7, 3)
-> partition(n, m - 1) is the subset of partition(n, m)

3. Find the relative
n = a, m = b
from partition(a,b) 
-> n = a - b, m = b
from partition(a - b, b)
-> n = a, m = b - 1
from partition(a, b - 1)

4. Generalize the pattern
partition(n, m) = partition(n - m, m) + partition(n, m - 1)
what if n < m -> Make the base case 0 if m = 0 or n < 0

5. Write code by combining all
partition(n, m) = { partition(n - m, m) + partition(n, m - 1)  &&  1 if n = 0  && 0 if m = 0 or n < 0  }

'''

def partition(n, m):
    if n == 0: 
        return 1
    elif m == 0 or n < 0: 
        return 0
    else:
        return partition(n - m, m) + partition(n, m - 1)
        


print(partition(9, 5))