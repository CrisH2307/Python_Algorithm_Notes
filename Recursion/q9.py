'''
Write a Python program to calculate the value of 'a' to the power of 'b' using recursion. 
'''
def power(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    if b == 1 or a == 1:
        return a 
    elif b > 1: 
        return a * power(a, b - 1)
    else:
        return power(a, b + 1) / a
    
print(power(3, 4))
