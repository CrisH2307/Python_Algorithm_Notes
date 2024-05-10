# DEQUE
'''
- Double Ended Queue is a type of queue in which insertion and removal of elements can either
be performed from the front or the rear. It does not follow FIFO rule

   Insertion/removal-  7   3   1   6   8   - Insertion/removal

- Types of Deque:
+ Input restricted deque: Input is restricted at a single end but allows deletion at both the ends.
+ Output ---------------: Output is restricted at a single end but allows insertion at both the ends.

Operation on a Deque:
- In a circular array, if the array is full, we start from the beginning.
But in a linear array implementation, if the array is full, no more elements can be inserted. 
In each of the operations below, if the array is full, "overflow message" is thrown.
Before performing the following operations, these steps are followed.
    1. Take an array (deque) of size n.
    2. Set two pointers at the first position and set front = -1 and rear = 0.
            0       1       2       3       4
           |
        Front = -1
        Rear = 0

1. Insert at the Front
+ Check the position of front. 
+ If front < 1, reinitialize front = n-1 (last index). 
+ Else, decrease front by 1.
+ Add the new key into array[front]

2. Insert at the Rear
+ Check if the array is full. 
+ If the deque is full, reinitialize rear = 0.
+ Else, increase rear by 1. 
+ Add the new key 5 into array[rear]. 

3. Delete from the Front
+ Check if the deque is empty. 
+ If the deque is empty (i.e. front = -1), deletion cannot be performed (underflow condition).
+ If the deque has only one element (i.e. front = rear), set front = -1 and rear = -1.
+ Else if front is at the end (i.e. front = n - 1), set go to the front front = 0.
+ Else, front = front + 1. 

4. Delete from the Rear
+ Check if the deque is empty. 
+ If the deque is empty (i.e. front = -1), deletion cannot be performed (underflow condition).
+ If the deque has only one element (i.e. front = rear), set front = -1 and rear = -1, else follow the steps below.
+ If rear is at the front (i.e. rear = 0), set go to the front rear = n - 1.
+ Else, rear = rear - 1. 

5. Check Empty
+ This operation checks if the deque is empty. If front = -1, the deque is empty.
+ This operation checks if the deque is full. If front = 0 and rear = n - 1 OR front = rear + 1, the deque is full.

'''
class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addRear(self, item):
        self.items.append(item)
    
    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



d = Deque()
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.items)