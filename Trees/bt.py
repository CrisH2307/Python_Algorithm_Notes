# Binary Tree Array Implementation
class Node:
    def __init__(self, data):
        self.data, self.children = data, [] # Children cannot be more than two element
    
    def add_node(self, data):
        if len(self.children) <= 1:
            self.children.append(Node(data))
            self.children.sort(key=lambda n: n.data)
        else:
            if data < self.children[0].data:
                self.children[0].add_node(data)
            elif data > self.children[1].data:
                self.children[1].add_node(data)
            else:
                return
    
    def display(self, level=0, prefix=""):
        # Print the current node with prefix for the connection
        print(prefix + f"{self.data}")

        if self.children:
            child_prefix = prefix + "   "

            for child in self.children:
                child_prefix = prefix + "|  "
                child.display(level + 1, child_prefix)

    def height(self):
        if not self.children:
            return 0
        return 1 + max(child.height() for child in self.children)


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    
    def add_node(self, data):
        self.root.add_node(data)

    def display(self):
        self.root.display()

    def height(self):
        return self.root.height() if self.root else 0
        

if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.add_node(8)
    tree.add_node(7)
    tree.add_node(9)
    tree.add_node(4)
    tree.add_node(-1)
    tree.add_node(10)
    tree.add_node(11)
    tree.display()
    print(tree.height())