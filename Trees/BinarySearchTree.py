# Binary Search Tree
'''
- A tree data structure for organizing and storing data in a sorted manner.
- Each node in a Binary Search Tree has at most two children, a left and a right child.
- Left child containing values less than the parent node
- The right child containing values greater than the parent node
- Allows for efficient searching insertion and deletion operations on the data stored in the tree

How to insert a value in a Binary Search Tree
- A new key is always inserted at the leaf by maintaining the property of the binary search tree.
- Start searching for a key from the root until we hit a leaf node.
- Once leaf node is found, the new node is added as a child of the leaf node
- Step by step:
    + Check the value to be inserted (X) with the value of the current node (val)
    --> If X < val, move to the left subtree
    --> Otherwise, move to the right subtree
    + Once the leaf node is reached, insert X to its right of left based on the relation between X and the leaf node's value

How to search a key in a Binary Search Tree
- We will start at the root, step by step:
    + Compate the value to be searched with the value of the root
    --> If its equal, done with the search. 
    --> If its smaller, go to the left subtree
    --> If its larger, go to the right subtree
    + Repeat the above step till no more traversal is possible
    + If at any iteration, key is found, return True. Else False

'''
import queue
# BST IMPLEMENTATION
class BST:
    class Node:
        def __init__(self, data=None, left=None, right=None) -> None:
            self.data = data
            self.left = left
            self.right = right

    # BST's init function
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        ...
    
    def search(self, data):
        ...
    
    def inorder_print(self):
        ...
    
    def pre_order_print(self):
        ...
    
    def breadthfirst_print(self):
        ...


# BST ITERATIVE METHOD
class BST:
    class Node:
        def __init__(self, data=None, left=None, right=None) -> None:
            self.data = data
            self.left = left
            self.right = right

    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            #curr points to the variable we are currently looking at
            curr = self.root
            inserted = False

            while not inserted:
                if data < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = BST.Node(data)
                        inserted = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(data)
                        inserted = True

    def search(self, data):
        curr = self.root

        while curr is not None:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
        
        return None

    
    def breadth_first_print(self):
        the_nodes = queue.Queue()

        if self.root is not None:
            the_nodes.put(self.root)
        
        while the_nodes:
            curr = the_nodes.get()

            if curr.left:
                the_nodes.put(curr.left)
            if curr.right:
                the_nodes.put(curr.right)

            print(curr.data, end="  ")
            


## INSERTING NODE
class Node:
    def __init__(self, key) -> None:
        self.left = self.right = None
        self.val = key
    
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = "  ")
        inorder(root.right)


if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Print inorder traversal of the BST
    inorder(r)

    '''
    OUTPUT:

        50
       /  \
      30   70
      / \ / \
     20 40 60 80
    
    '''


## SEARCHING NODE
class Node:
    def __init__(self, key) -> None:
        self.left = self.right = None
        self.key = key

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key == node.key:
        return node 
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    return node

def search(root, key):
    if root is None or root.key == key:
        return root
    
    if root.key < key:
        return search(root.right, key)
    
    return search(root.left, key)



if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
 
    # Key to be found
    key = 6
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
 
    key = 60
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")



## DELETETION IN TREE
'''
Case 1: Delete a leaf node
_ Assign that node into None

Case 2: Delete a Node in Single Child
_ Copy the child to the node and delete the node

'''