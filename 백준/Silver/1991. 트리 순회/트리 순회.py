import sys

def print_tree(tree):
    def preorder(node):
        if(node == "."):
            return
        print(node, end="")
        preorder(tree[node][0])
        preorder(tree[node][1])

    def inorder(node):
        if(node == "."):
            return
        inorder(tree[node][0])
        print(node, end="")
        inorder(tree[node][1])

    def postorder(node):
        if(node == "."):
            return
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end="")
    
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
    print()
    

test_case = (int)(sys.stdin.readline())
tree = {}


for _ in range(test_case):
    node, left, right = (sys.stdin.readline()).split()
    tree[node] = (left, right)
    
print_tree(tree)
