'''
Write a  Python program to calculate the sum of a list of numbers using recursion.
'''

def list_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + list_sum(arr[1:])

print(list_sum([10, 20, 30, 40, 50]))