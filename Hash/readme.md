# Hashing
### What is Hashing?
- A technique used in data structures to store and retrive data efficiently.
- Refers to the process of generating a fixed-size output from an input of variable size
using the mathematical formulas known as hash functions.

### How does Hasing work?
- Suppose we have a set of strings {“ab”, “cd”, “efg”} and we would like to store it in a table. 
- Main objective here is to search or update the values stored in the table quickly in O(1) time  and we are not concerned about the ordering of strings in the table

# Hash Table 
The Hash table data structure stores element in key-value pairs:
+ Key: Unique integer that is used for indexing the values.
+ Value: Data that are associated with keys.

            | Key | Data |


### Hashing (Hash Function)
- In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. The process is "Hashing"
- Let k be a key and h(x) be a hash function
-> Here, h(k) will give a new index to store the element linked with k.

#### Hash Collision
When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index)

Resolve the collision by: 
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
    + Open addressing; Linear, Quadratic probing and double hasing. Unlike chaining, open addressing doesn't store multiple elements into the same slot. Here, each  slot is either filled with a single key or left NIL.
