# HASHING
'''
What is Hashing?
- A technique used in data structures to store and retrive data efficiently.
- Refers to the process of generating a fixed-size output from an input of variable size
using the mathematical formulas known as hash functions.

How does Hasing work?
- Suppose we have a set of strings {“ab”, “cd”, “efg”} and we would like to store it in a table. 
- Main objective here is to search or update the values stored in the table quickly in O(1) time 
and we are not concerned about the ordering of strings in the table

'''

# Define a hash function
def simple_hash(key):
    return hash(key) % 10  # This is a very basic hash function for demonstration purposes

# Create an empty dictionary
toy_box = {}

# Add toys to the dictionary
toy_box[simple_hash("teddy bear")] = "Teddy Bear"
toy_box[simple_hash("ball")] = "Ball"
toy_box[simple_hash("car")] = "Toy Car"

# Now, let's say we want to find the toy "ball"
ball_key = simple_hash("ball")
if ball_key in toy_box:
    print("Found the toy:", toy_box[ball_key])
else:
    print("Toy not found.")

# Let's try to find a toy that doesn't exist, like "doll"
doll_key = simple_hash("doll")
if doll_key in toy_box:
    print("Found the toy:", toy_box[doll_key])
else:
    print("Toy not found.")
