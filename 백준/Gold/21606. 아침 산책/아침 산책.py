import sys
from collections import deque
# class node:
#     def __init__(self, value:int, type:bool):
#         self.value = value
#         self.type = type

class graph:
    nodelist = []
    node_type = []
    def __init__(self, size):
        self.nodelist = [None] * (size + 1)
        self.size = size
        self.node_type = [0] * (size + 1)
        input = sys.stdin.readline().strip()


        for i in range(1, size):
            data = list(map(int, sys.stdin.readline().split()))
            parent = int(data[0])
            child = int(data[1])
            if self.nodelist[parent] == None:
                self.nodelist[parent] = [(child)]
            else:
                self.nodelist[parent].append((child))
            if self.nodelist[child] == None:
                self.nodelist[child] = [(parent)]
            else:
                self.nodelist[child].append((parent))
            
            self.node_type[i] = int(input[i-1])
        self.node_type[-1] = int(input[-1])

    def print_graph(self):
        print(self.nodelist)
        print(self.node_type)
        
        
    def bfs(self, start):
        total = 0
        if self.node_type[start] == 0:
            return 0
        queue = deque()
        queue.append(start)

        visited = [False] * (self.size + 1)
        visited[start] = True

        while queue:
            # print(queue)
            vertex = queue.popleft()
            # print(vertex)
            # print("---------------------------------")
            for child_vertex in self.nodelist[vertex]:
                if self.node_type[child_vertex] == 1 and visited[child_vertex] == False:
                    total += 1
                    # print("count plus -> ",  total)
                    continue
                if visited[child_vertex] == False:
                    visited[child_vertex] = True
                    queue.append(child_vertex)
        return total

n = int(sys.stdin.readline())

Graph = graph(n)

count = 0
for i in range(n):
    # print("--------------------------------------------", i+1, "---------------------------------------")
    count += Graph.bfs(i+1)

print(count)




