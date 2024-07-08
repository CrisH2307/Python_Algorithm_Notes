'''
 Write a Python program to get the factorial of a non-negative integer using recursion.
'''
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))