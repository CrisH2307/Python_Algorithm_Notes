# CIRCULAR QUEUE
'''
- A extended version of a regular queue where the last element is connected to the first ele like a circle.
- It solves the major limitation of the normal queue. In a normal queue, after a bit of insertion and deletion, 
there will be non-usable empty space.

How does it work?
- Works by the process of circular increment when we try to increment the pointer and we reach the end
of the queue, we start from the beginning of the queue.
    if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue)

Circular Queue Operations
The circular queue work as follows:
    two pointers FRONT and REAR
    FRONT track the first element of the queue
    REAR track the last elements of the queue
    initially, set value of FRONT and REAR to -1

1. Enqueue Operation
    check if the queue is full
    for the first element, set value of FRONT to 0
    circularly increase the REAR index by 1 (i.e. if the rear reaches the end, next it would be at the start of the queue)
    add the new element in the position pointed to by REAR

2. Dequeue Operation
    check if the queue is empty
    return the value pointed by FRONT
    circularly increase the FRONT index by 1
    for the last element, reset the values of FRONT and REAR to -1
However, the check for full queue has a new additional case:
    Case 1: FRONT = 0 && REAR == SIZE - 1
    Case 2: FRONT = REAR + 1

The second case happens when REAR starts from 0 due to circular increment and when its value is just 1 less than 
FRONT, the queue is full.

'''
class CircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
    
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full")

        elif self.head == -1:
            self.head = self.tail = 0, 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
        
    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty")

        elif self.head = self.tail:
            temp = self.queue[self.head]
            self.head = self.tail = -1, -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
      
    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()





obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()

