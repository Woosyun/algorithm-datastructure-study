# 1. every node is either red or black
# 2. root is black
# 3. every leaf is black
# 4. if a node is red, then children are black
# 5. for each node, every path to leaves have same number of black nodes

class Node:
    def __init(self, value):
        self.parent = None
        self.value = value
        self.color = 0 # 0 for red, 1 for black
        self.left = None
        self.right = None

class RBTree:
    # node = (parent, value, color, left, right)
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        # assume right child is not None
        y = x.right
        x.right = None
    
        if x.parent is None: # x is root node
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y

        y.left = x
        x.parent = y
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if x.parent is None:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, value):
        # 1. insert node like binary tree
        # 2. color red
        # 3. rotate and re-color
        
        new_node = Node(value)
        y = None
        x = self.root
        while x is not None:
            y = x
            if x.value < value:
                x = x.right
            else:
                x = x.left
        
        if y is None:
            self.root = new_node
        else:
            new_node.parent = y
            if y.value < value:
                y.right = new_node
            else:
                y.left = new_node
        
        insert_fixup(new_node)
    
    def insert_fixup(self, x):
        while x.parent is not None and x.parent.color == 0: # parent is not leaf
            # 1. uncle is red => pp = red, p = black, uncle = black, insert_fixup(pp)
            # 2. uncle is black => p = black, left(right) rotate
            if x.parent.parent.left == x.parent:
                uncle = x.parent.parent.right # where is null check?
                if uncle.color == 0:
                    x.parent.color = 1
                    uncle.color = 1
                    x.parent.parent.color = 0
                    x = x.parent.parent 
                else:
                    if x == x.parent.right:
                        self.left_rotate(x.parent)
                    else:
                        x = x.parent
                    x.parent.color = 0
                    x.color = 1
                    self.right_rotate(x.parent)
            else:
                uncle = x.parent.parent.left
                if uncle.color = 0:
                    x.parent.color = 1
                    uncle.color = 1
                    x.parent.parent.color = 0
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        self.right_rotate(x.parent)
                    else:
                        x = x.parent
                    x.parent.color = 0
                    x.color = 1
                    self.left_rotate(x.parent)
        self.root.color = 1

    def delete(self, value):
        original_color = 0

        # 1. find target node
        x = self.root
        while x != None and x.value != value:
            if x.value > value:
                x = x.left
            else:
                x = x.right
        original_color = x.color

        # 2. remove
        if x.left != None and x.right != None:
            # choose minimum of right child tree
            y = find_minimum(x.right)
        elif x.left != None:
            y = x.left
        elif y.right != None:
            y = x.right
        else:
            y = None
        # swap y and x
        if y != None:
            y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x.parent.right == x:
            x.parent.right = y
        else:
            x.parent.left = y
        # remove x => ?

        #  3. if removed node is black, do something
        if original_color == 1:
            self.delete_fixup(y)

    def delete_fixup(self, x):
        #todo!
