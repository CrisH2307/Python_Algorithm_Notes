# Stack
A stack is kind of like an Array, but more resembles a stack of things in real life. You can plop things onto them and pop things off and that's it. It's LIFO. Last in first out. It's the opposite of how you want to stock a restaurant. It's more like a stack of plates.

![](https://www.sitesbay.com/data-structure/images/push-operation.gif)

Ex: The plates on top another

--> Put a new plate on top, remove the top plate
Adding elements to the top of stack and removing elements from the top of stack

### Basic Operations of Stack
+ Push: Add an element to the top of a stack
+ Pop: Remove an element from the top of a stack
+ IsEmpty: Check if the stack is empty
+ IsFull: Check if the stack is full
+ Peek: Get the value of the top element without removing it

```
class Stack:
     def __init__(self):
         self.container = []  
         
     def isEmpty(self):
         return self.container.size() == 0  

     def push(self, item):
         self.container.append(item)  
         
     def pop(self):
         return self.container.pop() 
         
     def size(self):
         return len(self.container) 
```

### Working of Stack Data Structure
The operations work as follows:
+ A pointer called TOP is used to keep track of the top element in the stack.
+ When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
+ On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
+ On popping an element, we return the element pointed to by TOP and reduce its value.
+ Before pushing, we check if the stack is already full
+ Before popping, we check if the stack is already empty


# Queue
A data structure to the data queue outside the hall, where the first person entering the
queue will get the first ticket. Its follow the First In First Out (FIFO) rule. Putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

![](https://miro.medium.com/v2/resize:fit:1400/0*2kyNa5cjR05cOs-0.gif)


### Basic Operations of Queue
+ A queue is an object (an abstract data structure - ADT) that allows the following operations:
+ Enqueue: Add an element to the end of the queue
+ Dequeue: Remove an element from the front of the queue
+ IsEmpty: Check if the queue is empty
+ IsFull: Check if the queue is full
+ Peek: Get the value of the front of the queue without removing it
```
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
```

### Working of Queue
```
Queue operations work as follows:
    two pointers FRONT and REAR
    FRONT track the first element of the queue
    REAR track the last element of the queue
    initially, set value of FRONT and REAR to -1

Enqueue Operation
    check if the queue is full
    for the first element, set the value of FRONT to 0
    increase the REAR index by 1
    add the new element in the position pointed to by REAR

Dequeue Operation
    check if the queue is empty
    return the value pointed by FRONT
    increase the FRONT index by 1
    for the last element, reset the values of FRONT and REAR to -1

```
### Limitation of Queue:
- After enqueuing or dequeuing, the size of the queue has been reduced
- We can only add indexes 0 and 1 only when the queue is reset.
- After REAR reaches the last index, if can store extra elements in the empty spaces(0 and 1), we can make use of the empty spaces. It is called Circular Queuee
