import sys
sys.setrecursionlimit(100000)

def same_parent(parent_node, x, y):
    x = find_parent(parent_node, x)
    y = find_parent(parent_node, y)

    if x == y :
        return False
    return True

def find_parent(parent_node, x):
    if parent_node[x] == x:
        return x
    else:
        parent_node[x] = find_parent(parent_node, parent_node[x])
        return parent_node[x]
    
def union(parent_node, x, y):
    x = find_parent(parent_node, x)
    y = find_parent(parent_node, y)
    if x != y:
        parent_node[y] = x




v, e = map(int, sys.stdin.readline().split())



nodes = []
parent_node = [i for i in range(v+1)]
# print(parent_node)
for i in range(e):
    nodes.append(list(map(int, sys.stdin.readline().split())))
    
nodes = sorted(nodes, key= lambda x: x[2])

mst_graph = []
for node in nodes:
    if same_parent(parent_node, node[0], node[1]):
        mst_graph.append(node)
        union(parent_node, node[0], node[1])

sum = 0
for node in mst_graph:
    sum += node[2]

print(sum)

    