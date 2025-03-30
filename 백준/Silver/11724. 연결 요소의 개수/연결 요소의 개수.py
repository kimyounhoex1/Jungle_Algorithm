import sys
sys.setrecursionlimit(10**6)
class Graph:
    
    nodelist = []
    visited = []
    def __init__(self, n:int, m:int):
        self.nodelist = [None] * n
        self.visited = [False] * n
        self.n = n
        self.m = m
        
        for _ in range(m):
            input = sys.stdin.readline().split()
            # print(input[0], ",", input[1])

            if self.nodelist[int(input[0])-1] == None:
                self.nodelist[int(input[0])-1] =[int(input[1])]
            else:
                self.nodelist[int(input[0])-1].append(int(input[1]))
            if self.nodelist[int(input[1])-1] == None:
                self.nodelist[int(input[1])-1] =[int(input[0])]
            else:
                self.nodelist[int(input[1])-1].append(int(input[0]))

        
    def DFS(self, v):
        if self.nodelist[v-1] == None:
            self.visited[v-1] = True
            return
        
        self.visited[v-1] = True
        for vertex in self.nodelist[v-1]:
            if self.visited[vertex-1] == False:
                self.visited[vertex-1] = True
                self.DFS(vertex)

    def print_DFS(self):
        print(self.nodelist)

    def All_DFS(self):
        cnt = 0
        while self.visited.count(False) != 0:
            # print(self.visited)
            vertex = self.visited.index(False)+1
            
            self.DFS(vertex)
            cnt += 1
        
        return cnt


input = sys.stdin.readline().split()

graph = Graph(int(input[0]), int(input[1]))

# graph.print_DFS()
print(graph.All_DFS())