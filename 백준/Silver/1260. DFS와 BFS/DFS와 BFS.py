import sys
from collections import deque
class Graph:
    nodelist = []
    dfs_visited = []
    def __init__(self, N: int, M: int, V:int):
        self.nodelist = [None] * (N + 1)
        self.dfs_visited = [False] * (N + 1)
        self.N = N
        self.M = M
        self.V = V

    def insert_data(self):
        for i in range(self.M):
            input = sys.stdin.readline().split()
            if self.nodelist[int(input[0])] == None:
                self.nodelist[int(input[0])] = [int(input[1])]
            else:
                self.nodelist[int(input[0])].append(int(input[1]))
            if self.nodelist[int(input[1])] == None:
                self.nodelist[int(input[1])] = [int(input[0])]
            else:
                self.nodelist[int(input[1])].append(int(input[0]))
        # print(self.nodelist)
        for vertexlist in self.nodelist:
            if vertexlist == None:
                continue
            vertexlist.sort()

    def BFS(self, v):
        visited = [False] * (self.N + 1)
        queue = deque()
        queue.append(v)
        visited[v] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            if not self.nodelist[v]:
                return
            for i in range(len(self.nodelist[vertex])):
                # print(self.nodelist[vertex][i])
                if visited[self.nodelist[vertex][i]] == False:
                    queue.append(self.nodelist[vertex][i])
                    visited[self.nodelist[vertex][i]] = True
                    
    def start_BFS(self):
        self.BFS(self.V)
        
    def DFS(self, v):
        # print(self.dfs_visited)
        if self.dfs_visited[v] == True:
            return
        print(v, end = " ")
        self.dfs_visited[v] = True
        if not self.nodelist[v]:
            return
        for vertex in self.nodelist[v]:
            self.DFS(vertex)
        
    def start_DFS(self):
        self.DFS(self.V)
                
N, M, V = map(int, sys.stdin.readline().split())

graph = Graph(N, M, V)
graph.insert_data()
graph.start_DFS()
print()
graph.start_BFS()