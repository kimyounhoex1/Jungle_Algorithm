import sys
from collections import deque

class graph:
    nodelist = []
    parentnode = []
    def __init__(self, n: int):
        self.nodelist = [None] * n
        self.n = n
        self.parentnode = [None] * (n-1)

        for i in range(self.n -1 ):
            input = sys.stdin.readline().split()
            if self.nodelist[int(input[0])-1] == None:
                self.nodelist[int(input[0])-1] = [int(input[1])]
            else:
                self.nodelist[int(input[0])-1].append(int(input[1]))
            if self.nodelist[int(input[1])-1] == None:
                self.nodelist[int(input[1])-1] = [int(input[0])]
            else:
                self.nodelist[int(input[1])-1].append(int(input[0]))
            
    # def print_graph(self):
    #     print(self.nodelist)

    def BFS(self, v):
        visited=[False] * self.n
        visited[v-1] = True
        queue = deque()
        queue.append(v)

        while queue:
            parent_vertex = queue.popleft()
            for child_vertex in self.nodelist[parent_vertex - 1]:
                if visited[child_vertex - 1] == False:
                    queue.append(child_vertex)
                    visited[child_vertex - 1] = True
                    self.parentnode[child_vertex-2] = parent_vertex
            
    def print_parent(self):
        for i in self.parentnode:
            print(i, end=" ")

input = int(sys.stdin.readline())

Graph = graph(input)
Graph.BFS(1)
Graph.print_parent()