def inorder_tree_walk(x):
    inorder_tree_walk(x.left)
    print(x.value, end='')
    inorder_tree_walk(x.right)

class Node:
    def __init__(value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__():
        self.root = None

    def insert(v):
        new_node = Node(v)

        parent = None
        child = self.root
        while child is not None:
            parent = child
            if child.value < v:
                child = child.right
            else:
                child = child.left

        # tree is empty
        if parent is None:
            self.root = new_node
        else:
            if parent.value < v:
                parent.right = new_node
            else:
                parent.left = new_node

