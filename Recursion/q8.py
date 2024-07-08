'''
Fibonacci sequence using recursion
'''

def fibonacci(num):
    if num == 1 or num == 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(7))