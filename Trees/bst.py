import queue

class BST:
    def __init__(self, data=None):
        self.data, self.left, self.right = data, None, None
    
    def insert(self, data):
        if not self.data:
            self.data = data
        elif data < self.data:
            if not self.left:
                self.left = BST(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if not self.right:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def search(self, data):
        found = False
        if self.data:
            if self.data == data:
                found = True
            elif self.data > data and self.left:
                found = self.left.search(data)
            elif self.data < data and self.right:
                found = self.right.search(data)
        return found
    
    def find_height(self):
        value = 0
        if self.data:
            left, right = 0, 0
            if self.left:
                left = self.left.find_height()
            if self.right:
                right = self.right.find_height()
            value = (right if right > left else left) + 1
        return value

    #-----Printing Functions------
    def inorder_print(self):
        # Print values from smallest to largest
        if self.data:
            if self.left:
                self.left.inorder_print()
            print(self.data, end=" ")
            if self.right:
                self.right.inorder_print()
    
    def pre_order_print(self):
        # Print values from smallest to largest, node data is first
        if self.data:
            print(self.data, end=" ")
            if self.left:
                self.left.pre_order_print()
            if self.right:
                self.right.pre_order_print()

    def post_order_print(self):
        # Print values from smallest to largest, node data is last
        if self.data:
            if self.left:
                self.left.post_order_print()
            if self.right:
                self.right.post_order_print()
            print(self.data, end=" ")

    def breadth_first_print(self):
        node = queue.Queue()

        if self.data:
            node.put(self)
        
        while not node.empty():
            curr = node.get()

            if curr.left:
                node.put(curr.left)
            if curr.right:
                node.put(curr.right)

            print(curr.data, end="")


    def print_tree(self, prefix, is_left=False):
        '''Prints a string representation of the actual tree.'''
        if self.data:
            print(prefix, end="")
            print("|__" if is_left else "|---", end="")
            print(self.data)
            # Enter the next tree level - left and right branch
            if self.left:
                self.left.print_tree(prefix + ("|   " if is_left else "    "), True)
            if self.right:
                self.right.print_tree(prefix + ("|   " if is_left else "    "), False)


if __name__ == "__main__":
    bst = BST(6)
    bst.insert(7)
    bst.insert(10)
    bst.insert(1)
    bst.insert(3)
    bst.insert(-4)
    bst.insert(19)

    bst.print_tree("")

    print(f"Is 10 in the our BST? {bst.search(10)}")
    print(f"Is -1 in the our BST? {bst.search(-1)}")

    print("Printing the BST with breadth first...")
    bst.breadth_first_print()
    print()

    print("Printing the BST in order...")
    bst.inorder_print()
    print()

    print("Printing the BST pre-ordered...")
    bst.pre_order_print()
    print()

    print("Printing the BST post-ordered...")
    bst.post_order_print()
    print()

    print(f"The height (max depth) of this tree is: {bst.find_height()}")
