# Red-Black Trees
'''
Augmented Data Structure
Uses coloring rules to maintain shape
+ Not perfectly balanced
+ Not height balance
+ Longest branch of red-black is at most twice as long as the shortest branch of tree

Coloring rules
1. Every node is red or black
2. The root is always black
3. A red node cannot have red children
    - a red node always have a black parent
4. Starting from any node in the tree, the number of black nodes between that node and any null-leaf
within its subtree must be the same 

Insertion Algorithm:
1. Find insertion position just like a regular BST
2. New nodes are always added as red nodes so rule 4 is never broken
3. Go backup the tree looking for breaking of rule 2 and 3 and apply fixes as we go.
Note that this starts at insertion point and works up the tree just like AVL trees.


Fixes, when we might break rule 2,3 but we never break rule 1 and 4;
- If rule 2 (root must be black) is broken:
    + Change the root from red to black
    + This adds 1 extra black node to every branch
    + Do not break rule 4

- If rule 3 (red node cannot have red child) is broken:
    - Identify the 3 nodes in the B-r-r chain of nodes
        + The top black node is called the grandparent (G)
        + The upper red node is called the parent (P)
        + The lower red node is called the child (C)
        + Find the Sibling (S) of the parent (note.. parent, not child !)
                + Null-leaf are considered to be black so if sibling does not
                exist then it is black.
                + If Sibling is Red:
                    - Swap the grandParent node's colour with the parent
                    and sibling node's colour. In other words, Grandparent(G)
                    becomes red, Parent(P) and Sibling(S) becomes black
                + If Sibling is Black:
                    - Perform either a zig-zag or zig-zag rotaion depending 
                    on configuration of G-P-C
                    - Zig-zig is basically a single rotation with an exchange 
                    of colours where P becomes black and G becomes red
                    - Zig-zag is basically a double rotation with an exchange
                    of colours where C becomes black and G becomes red




'''