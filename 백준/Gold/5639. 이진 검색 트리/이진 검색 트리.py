import sys
sys.setrecursionlimit(2*10**5)
class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class binary_tree:
    def __init__(self):
        self.root = None
    
    def add(self, node):
        if self.root is None:
            self.root = node
            return
        cur = self.root
        while cur:
            if node.val > cur.val:
                if cur.right == None:
                    cur.right = node
                    return
                else:
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = node
                    return
                else:
                    cur = cur.left 

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)
    
    def postorder_print(self):
        self.postorder(self.root)
    

bitree = binary_tree()

while True:
    try:
        number = int(sys.stdin.readline())
        bitree.add(node(number))
    except ValueError:
        break

bitree.postorder_print()