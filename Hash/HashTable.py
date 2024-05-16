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