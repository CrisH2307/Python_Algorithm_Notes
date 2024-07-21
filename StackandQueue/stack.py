# STACK
'''
- A stack is a linear data structure that follows the priciple of First In Last Out (FILO)
Ex: The plates on top another
--> Put a new plate on top, remove the top plate
Adding elements to the top of stack and removing elements from the top of stack


Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it

Working of Stack Data Structure
The operations work as follows:
+ A pointer called TOP is used to keep track of the top element in the stack.
+ When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
+ On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
+ On popping an element, we return the element pointed to by TOP and reduce its value.
+ Before pushing, we check if the stack is already full
+ Before popping, we check if the stack is already empty

'''
# def Stack():
#     stack = []
#     return stack

# def check_empty(stack):
#     return len(stack) == 0

# def push(stack, item):
#     stack.append(item)

# def pop(stack):
#     if check_empty(stack):
#         return "Stack is empty"

#     return stack.pop()

# stack = Stack()
# push(stack, str(1))
# push(stack, str(2))
# push(stack, str(3))
# push(stack, str(4))
# print("popped item: " + pop(stack))
# print("stack after popping an element: " + str(stack))

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
if __name__ == '__main__':
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(8)
    s.push(4)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())


