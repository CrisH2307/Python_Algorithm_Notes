# Queue
'''
- A data structure to the data queue outside the hall, where the first person entering the
queue will get the first ticket. Its follow the First In First Out (FIFO) rule.
_ Putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

Basic Operations of Queue
+ A queue is an object (an abstract data structure - ADT) that allows the following operations:
+ Enqueue: Add an element to the end of the queue
+ Dequeue: Remove an element from the front of the queue
+ IsEmpty: Check if the queue is empty
+ IsFull: Check if the queue is full
+ Peek: Get the value of the front of the queue without removing it

Working of Queue

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


Limitation of Queue:
- After enqueuing or dequeuing, the size of the queue has been reduced
- We can only add indexes 0 and 1 only when the queue is reset.
- After REAR reaches the last index, if can store extra elements in the empty spaces(0 and 1),
we can make use of the empty spaces. It is called Circular Queuee

'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None     
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()
