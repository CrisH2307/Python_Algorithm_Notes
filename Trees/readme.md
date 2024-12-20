# Tree
### What is Tree ?
- Tree data structure is a specialized data structure to store data in hierarchical manner.
- It is used to organize and store data in the computer to be used more effectively.
- It consists of a central node, structural nodes, and sub-nodes, which are connected via edges.
- Like roots, branches, and leaves connected

![](https://miro.medium.com/v2/resize:fit:1280/1*GT9oSo0agIeIj6nTg3jFEA.gif)

Easy to Understand:
- A hierachial structure that is used to represent and organize data in a way that is easy to navigate and search
- A collection of nodes that are connected by edges and has a hierarchical relationship between the nodes
- The topmost node: Root
- The nodes below root: Child Nodes
- Each node can have multiple child nodes
- Child nodes can have their own child nodes, forming a recursive structure

Why Tree is a considered a non-linear data structure ????
- The data in a tree are not stored in a sequential manner, they are not stored linearly.
- Instead, they are arranged on multiple levels or we can say it is a hierarchical structure

Terminologies (Look in the Image):
- A non-empty tree must contain exactly one root node and exactly one path from the root to all other nodes of the tree
- Parent Node: The node which is a predecessor of a node is called the parent node of that node.
---> B is the parent node of D and E
- Child Node: The node which is the immediate successor of a node is called the child node of that node
---> D and E are the child node of B
- Root Node: The topmost node of a tree or the node which does not have any parent node is called the root node
---> A is the root node
- Leaf Node or External Node: The nodes which do not have any child nodes are called leaf nodes.
---> K,L,M,N,O,P,G are the leaf nodes of the tree
- Ancestor of a Node: Any predecessor nodes on the path of the root to that node are called Ancestors of that node
---> A, B are the ancestor nodes of the node E
- Descendant: A node x is a descendant of another node y if and only if y is an ancestor of x
- Sibling: Children of the same parent node are called siblings.
---> D, E are siblings
- Level of a node: The count of edges on the path from the root node to that node
---> The root node is the level 0
- Subtree: Any node of the tree along with its descendant

Representation of Tree
- A tree consist a root node, and zero or many subtrees T1, T2,..., Tk such that there is an edge from the root node of each subtree. Subtree of a node X consists of all the nodes which have node X as ancestor node.

Importance of Tree Data Structure:
- Store information that naturally forms a hierarchy. Ex: File system
- Provide moderate access/search quicker than Linked List but slower than arrays
- Provide moderate insertion/deletion quicker than Arrays and slower than unordered linked list
- Tree dont have an upper limit on the number of nodes as nodes are linked using pointers


### Perfectly Balanced Trees
- Number of nodes in left/right subtrees differ by no more than 1 for all nodes in tree(not just root)
- If at any node the number of nodes in left/right subtrees differ by more than 1, the entire tree isn't perfectly balanced.

### Height Balanced Trees
- Height of left/right subtrees differ by no more than 1 for all nodes in tree (not just root)
- If at any node the height of the left/right subtrees differ by more than 1, the entire tree isn't height balanced


# AVL Tree
- Height balanced binary search trees
- Each node must maintain extra information that allows us to find the balance of a node without having to calculate the heights

` NodeBalance = Height of Right Subtree - Height of Left Subtree `
+ Positive balance means right subtree is taller
+ Negative balance means left subtree is taller

### Insertion algorithm
- Start with basic BST insertion algorithm
- After insert a node, move up the tree starting from the inserted node's parent and check its balance.
- If balance of node is not 0, +1, or -1, we must fix the tree by performing a rotation.
- There are two types of rotation.
+ Single rotation
+ Double rotation
+ To determine which to use we look at the sign of the balance of the one that is off balanced (the one with +/-2) and the sign of the balance on its taller child
    + If both balance have the same sign, use single rotation
    + If the balances have different sign, use double rotation
- Continue back up the tree until the root is reached, rotating as necessary.
