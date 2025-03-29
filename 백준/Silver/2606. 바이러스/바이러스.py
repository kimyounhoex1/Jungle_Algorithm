import sys
from collections import deque

class graph:
    nodelist = []
    visited = []
    def __init__(self, n: int, e: int):
        self.nodelist = [None] * (n + 1)
        self.visited = [False] * (n + 1)
        self.n = n
        self.e = e

        for _ in range(e):
            input = sys.stdin.readline().split()
            if self.nodelist[int(input[0])] == None:
                self.nodelist[int(input[0])] = [int(input[1])]
            else:
                self.nodelist[int(input[0])].append(int(input[1]))

            if self.nodelist[int(input[1])] == None:
                self.nodelist[int(input[1])] = [int(input[0])]
            else:
                self.nodelist[int(input[1])].append(int(input[0]))
    
    # def graph_print(self):
        # print(self.nodelist)

    def DFS(self, v):
        count = 0
        # print(v)
        if self.nodelist[v] == None:
            return 0
        self.visited[v] = True

        for adj in self.nodelist[v]:
            if self.visited[adj] == False:
                # print(adj)
                self.visited[adj] == True
                count += (1 + self.DFS(adj))
                # print(count)
        
        return count
                

    def start_DFS(self):
        return self.DFS(1)

n = int(sys.stdin.readline())
e = int(sys.stdin.readline())

Graph = graph(n, e)

# Graph.graph_print()

print(Graph.start_DFS())

