# DEPTH-FIRST SEARCH (DFS)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None

'''
1. Preorder Traversal (root-left-right)
- Visit the current/root node before visiting any nodes inside the left or right subtress.
- The traversal is root - left child - right child.
- It means that the root node is traversed first then its left child and finally the right child

Representation:
+ Follow step 2 to 4 until root != None
+ Write root.data
+ Preorder (root -> left / root.left)
+ Preorder (root -> right / root.right)
+ End loop

'''

def printPreorder(root):
    if root is None:
        return
    
    # Deal with the node
    print(root.data, end= ' ')

    # Recur on the left subtree
    printPreorder(root.left)

    # Recur on the right subtree
    printPreorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreorder(root)

    '''
    Output 
    1 2 4 5 3 6     

         1
        / \
       2   3
      / \   \
     4   5   6
    
    Explaination:
    + At first, the root will be visited is 1
    + After this, traverse in the left subtree. Now the left subtree is visited -> Node 2 is visited
    + Again the left subtree of node 2 in traversed and the root of the tree -> Node 4 is visited
    + There is no subtree of 4 and the left subtree of node 2 is visited. So now the right subtree
    of node 2 will be traversed and the root of the subtree -> node 5 will be visited
    + The left subtree of node 1 is visited. So now the right subtree of node 1 will be 
    traversed -> node 3 is visted
    + Now node 3 has no left subtree. So the right subtree will be traversed and the root of the subtree, 
    node 6 will be visited. After the there is no node that is not yet traversed, to the traversal ends.

    ==> 1 -> 2 -> 4 -> 5 -> 3 -> 6

    '''


'''
2. Inorder Traversal (left-root-right)
- The left subtree is traversed first
- Then the root node for that subtree is traversed
- Finally, the right subtree is traversed

Representation:
+ Follow step 2 to 4 until root != None
+ Inorder (root->left / root.left)
+ Write root->data / root.data
+ Inorder(root->right / root.right)
+ End loop

'''
def printInorder(root):
    if root is None:
        return
    
    # First recur on left subtree
    printInorder(node.left)

    # Now deal with the node
    print(node.data, end=' ')

    # Then recur on right subtree
    printInorder(node.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
 
    # Function call
    print("Inorder traversal of binary tree is:")
    printInorder(root)

    '''
    Output:
    4   2   5   1   3   6

    Explaination:
    + Traversal will go from 1 to its left subtree, node 2. Then from node 2 to its left subtree
    root, node 4. Now node 4 has no left subtree, so it will be visited. It also does not have any
    right subtree. So no more traversal from 4
    + As the left subtree of 2 is visited completely, now it read data of node 2 before moving 
    to its right subtree.
    + Now the right subtree of 2 will be traversed move to node 5. For node 5, there is no left subtree,
    so it gets visited and after that, the traversal comes back because there is no right subtree of node 5.
    + As the left subtree of node 1 is, the root itself, node 1 will be visited
    + Left subtree of node 1 and the node itself is visited. So now the right subtree of 1 will be traversed,
    move to node 3. As node 3 has no left subtree so it gets visited
    + The left subtree of node 3 and the node itself is visited. So traverse to the right subtree and visit
    node 6. Now the traversal ends as all the nodes are traversed.

    4 -> 2 -> 5 -> 1 -> 3 -> 6

    '''


'''
3. Postorder Traversal (left-right-root)
- The left subtree is traversde first
- Then the right subtree is traversed
- Finally, the root node of the subtree is traversed

Representation:
+ Follow step 2 to 4 until root != None
+ Postorder (root->left / root.left)
+ Postorder (root->right / root.right)
+ Write root->data / root.data
+ End loop

'''
def printPostorder(root):
    if node == None:
        return
    
    # First recur on left subtree
    printPostorder(node.left)

    # Then recur on right subtree
    printPostorder(node.right)

    print(node.data, end=' ')


# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
 
    # Function call
    print("Postorder traversal of binary tree is:")
    printPostorder(root)

    '''
    Output: 
    4   5   2   6   3   1

    Explaination:
    + The traversal will go from 1 to its left subtree, node 2, then from 2 to its left subtree
    root, node 4. Now node 4 has no subtree, so it will be visited.
    + As the left subtree of node 2 is visited, now it will traverse the right subtree of 2, it will 
    move to 5. As there is no subtree of 5, it will be visited
    + Now both the left and right subtrees of node 2 are visited. So now visit node 2 itself.
    + As the left subtree of node 1 is traversed, it will now mvoe to the right subtree root. Node 3
    does not have any left subtree, so it traverse the right subtree, node 6. Node 6 has no subtree and
    so it is visited.
    + All the subtrees of node 3 are traversed. So now node 3 is visited
    + As all the subtrees of node 1 are traversed, now it is time for node 1 to be visited and traversal
    ends after that as the whole tree is traversed.

    4 -> 5 -> 2 -> 6 -> 3 -> 1
    
    '''