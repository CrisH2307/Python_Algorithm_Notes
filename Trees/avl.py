class AVL:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = 1

        # Return the balance of the node
        def balance(self):
            heightRight = self.right.height if self.right else 0
            heightLeft = self.left.height if self.left else 0
            return heightRight - heightLeft
        
        # Update the height of the node
        def updateHeight(self):
            heightRight = self.right.height if self.right else 0
            heightLeft = self.left.height if self.left else 0
            self.height = 1 + max(heightRight, heightLeft)
    
    def __init__(self):
        self.root = None

    def insert(self, subtree, data):
        # Standard BST insertion
        if subtree is None:
            return self.Node(data)
        
        if data < subtree.data:
            subtree.left = self.insert(subtree.left, data)
        else:
            subtree.right = self.insert(subtree.right, data)

        # Balance the node if it has become unbalanced
        subtree.updateHeight()
        
        balance = subtree.balance()
        if balance == 2:  # Right side is heavier
            if subtree.right and subtree.right.balance() == -1:
                subtree.right = self.rightRotate(subtree.right)
            subtree = self.leftRotate(subtree)
        elif balance == -2:  # Left side is heavier
            if subtree.left and subtree.left.balance() == 1:
                subtree.left = self.leftRotate(subtree.left)
            subtree = self.rightRotate(subtree)

        return subtree

    def leftRotate(self, A):
        B = A.right
        A.right = B.left
        B.left = A
        A.updateHeight()
        B.updateHeight()
        return B

    def rightRotate(self, A):
        B = A.left
        A.left = B.right
        B.right = A
        A.updateHeight()
        B.updateHeight()
        return B

    def insertRecursive(self, data):
        self.root = self.insert(self.root, data)

    def print_inorder(self, node):
        if node is not None:      
            self.print_inorder(node.left)
            print(node.data, end=" ")
            self.print_inorder(node.right)

    def printBreadthFirst(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            print(curr.data, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

if __name__ == '__main__':
    tree = AVL()
    
    tree.insertRecursive(10)
    tree.insertRecursive(20)
    tree.insertRecursive(25)
    tree.insertRecursive(30)
    tree.insertRecursive(40)
    tree.insertRecursive(50)
    
    print("In-order Traversal:")
    tree.print_inorder(tree.root)
    print("\nBreadth-First Traversal:")
    tree.printBreadthFirst()
    print("\n")
