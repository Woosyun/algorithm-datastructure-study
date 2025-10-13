# 1. BTree has t..=2*t children
#   ex) if t=2, 234 tree
# 2. 

class BTree:
    def __init__(t):
        self.root = None
        self.t = t

    def search(self, k):
        return search(self.root, k)
    
    def split(self, x, i):
        if self.root == x:
            self.root = Node()
            self.root.children.append(x)
            split(self.root, x)
        else:
            split(x, 

class Node:
    def __init__():
        self.children = [] # child: Key
        self.keys = []
        self.leaf = True

def search(x, k):
    i = 0
    while i < len(x.keys) and k > x.keys[i]:
        i += 1

    # 끝 노드는 하나?
    if i < len(x.keys) and k == x.keys[i]:
        return (x, i)
    elif x.leaf == True:
        return None
    else:
        next_x = disk_read(x.keys[i])
        return search(next_x, k)

def disk_read(key):
    # todo
    return None
def disk_write(Node):
    # todo
    return None
