from bt import *

def heapify(node):
    if node.children:
        largest_child = max(node.children, key=lambda n: n.data)
        largest = largest_child if largest_child.data > node.data else node

        if largest != node:
            heapify(largest)
            node.data, largest.data = largest.data, node.data
        
        for child in node.children:
            heapify(child)


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
    print("---------------------------------------")

    heapify(tree.root)
    tree.display()