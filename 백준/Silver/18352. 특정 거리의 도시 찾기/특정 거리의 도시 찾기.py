import sys
from collections import deque

class graph:
    nodelist = []
    target_distance = []
    def __init__(self, n:int, m:int, k:int, x:int):
        self.n = n
        self.m = m
        self.k = k
        self.x = x
        self.nodelist = [None] * (n)
        self.target_distance = [0] * n

        for _ in range(self.m):
            input = sys.stdin.readline().split()
            if self.nodelist[int(input[0]) - 1] == None:
                self.nodelist[int(input[0]) - 1] = [int(input[1])]
            else:
                self.nodelist[int(input[0])-1].append(int(input[1]))

        
    # def print_graph(self):
    #     print(self.nodelist)

    def DFS(self, start):
        visited = [False] * self.n
        visited[start-1] = True
        queue = deque()
        queue.append((start, 0))
        dist = 1
        while queue:
            
            vertex = queue.popleft()
            self.target_distance[vertex[0]-1] = vertex[1]
            if self.nodelist[vertex[0] - 1] == None :
                if visited[vertex[0]-1] == False:
                    print("vertex = " , vertex[0])
                    visited[vertex[0]-1] = True
                    self.target_distance[vertex[0]-1] = dist
                    continue
                
            else:
                for v in self.nodelist[vertex[0] - 1]:
                    if visited[v-1] == False:
                        queue.append((v, vertex[1] + 1))
                        visited[v-1] = True
                        self.target_distance[v-1] = dist
            
    def print_dist(self):
        if self.k not in self.target_distance:
            print(-1)
            return
        for i in range(len(self.target_distance)):
            if self.target_distance[i] == self.k:
                print(i+1)
            
        

input = list(map(int, sys.stdin.readline().split()))

Graph = graph(input[0], input[1], input[2], input[3])

# Graph.print_graph()
Graph.DFS(input[3])
Graph.print_dist()
