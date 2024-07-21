'''
Given a string S, the task is to write a program to print all permutations of a given string. 

Input: S = “ABC”
Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”

'''
def permute(a, start, end):
    if start == end:
        print(''.join(a))
    for i in range(start, end):
        a[start], a[i] = a[i], a[start]
        permute(a, start + 1, end)
        a[start], a[i] = a[i], a[start]



string = "ABC"
n = len(string) 
a = list(string) 
  
# Function call 
permute(a, 0, n) 