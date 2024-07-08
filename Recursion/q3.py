'''
Write a recursive function that given an input n sums all nonnegative integers up to n

Ex:
sum(0) -> 0
sum(4) -> 1 + 2 + 3 + 4 = 10
sum(n) -> 1 + 2 + 3 + 4 + ... + n

Explain:
1. Simplest possible input
    sum(0) => 0 
    Base case 0 if n = 0

2. Visualize input
    n = 1
    .

    n = 2
    .
    . .

    n = 3
    .
    . .
    . . .

    n = 4
    . 
    . .
    . . .
    . . . .

    n = 5 
    .
    . .
    . . . 
    . . . .
    . . . . .

3. Ralate hard cases to simpler cases -> Find the relative 
- Ask yourself, hey if I was given the answer to n = 4 case, could I solve the problem of n = 5 case ?
-> When we know the ans of n = 4 case, we just need to add 5 on the n = 5 case

4. Generalize the pattern
n = k     n = k - 1
sum(k) =  sum(k - 1) + k

5. Write code by combining recursive pattern with the base case

sum(n) = ( sum(n - 1) + n && 0 if n = 0 )


'''
def sumre(n):
    if n == 0: return 0
    return n + sumre(n - 1)

print(sumre(4))
