# HASH TABLE
'''
- The Hash table data structure stores element in key-value pairs 
    + Key: Unique integer that is used for indexing the values
    + Value: Data that are associated with keys
        | Key | Data |

Hashing (Hash Function)
- In a hash table, a new index is processed using the keys. And, the element 
corresponding to that key is stored in the index. The process is "Hashing"
- Let k be a key and h(x) be a hash function
-> Here, h(k) will give a new index to store the element linked with k.

Hash Collision
- When the hash function generates the same index for multiple keys, there will be
a conflict (what value to be stored in that index)
- Resolve the collision by: 
    + Collision resolution by chaining: If a hash function produces the same index 
    for multiple elements, these elements are stored in the same index by using a 
    doubly-linked list. If j is the slot for multiple elements, it contains a pointer 
    to the head of the list of elements. If no element is present, j contains None.
        chainedHashSearch(T, k)
            return T[h(k)]
        chainedHashInsert(T, x)
            T[h(x.key)] = x //insert at the head
        chainedHashDelete(T, x)
            T[h(x.key)] = None
    + Open addressing; Linear, Quadratic probing and double hasing. Unlike chaining, 
    open addressing doesn't store multiple elements into the same slot. Here, each 
    slot is either filled with a single key or left NIL.



'''

hashTable = [[], ] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return False
    
    for i in range(2, n//2):
        if n % i == 0:
            return False
    
    return True

def getPrime(n):
    if n % 2 == 0:
        n = n + 1
    while not checkPrime(n):
        n += 2
    
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    idx = hashFunction(key)
    hashTable[idx] = [key, data]

def removeData(key):
    idx = hashFunction(key)
    hashTable[idx] = 0


insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

removeData(123)

print(hashTable)





# IMPLEMENTATION AS A CLASS
'''
- A hash table allows for quick insertion, deletion and retrieval of data
- Seperate chaining is a technique used to handle collisions in a hash table.
When two or more keys map to the same index in the array, we store them in a 
linked list at that index. It allows us to store multiple values at the same
index and still be able to retrive them using their key.


'''

class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key) -> int:
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
    
    def search(self, key):
        index = self._hash(key)

        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        prev = None
        curr = self.table[index]
        
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[index] = curr.next
                self.size -= 1
                return
            prev = curr
            curr = curr.next
        
        raise KeyError(key)
    
    def __str__(self) -> str:
        elements = []
        for i in range(self.capacity):
            curr = self.table[i]
            while curr:
                elements.append((curr.key, curr.value))
                curr = curr.next
        return str(elements)

if __name__ == '__main__': 
  
    # Create a hash table with 
    # a capacity of 5 
    ht = HashTable(5) 
  
    # Add some key-value pairs 
    # to the hash table 
    ht.insert("apple", 3) 
    ht.insert("banana", 2) 
    ht.insert("cherry", 5) 
  
    # Check if the hash table 
    # contains a key 
    print("apple" in ht)  # True 
    print("durian" in ht)  # False 
  
    # Get the value for a key 
    print(ht.search("banana"))  # 2 
  
    # Update the value for a key 
    ht.insert("banana", 4) 
    print(ht.search("banana"))  # 4 
  
    ht.remove("apple") 
    # Check the size of the hash table 
    print(len(ht))  # 3 