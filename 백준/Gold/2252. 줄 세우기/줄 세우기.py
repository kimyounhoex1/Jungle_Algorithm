import sys
from collections import deque

def topology_sort(nodelist, indegree):
    result = []
    q = deque()

    for i in range(1, len(indegree)):
        # print(i)
        if indegree[i] == 0:
            q.append(i)

    while q:
        
        vertex = q.popleft()
        result.append(vertex)

        
        for node in nodelist[vertex]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

    return result

n, m = map(int, sys.stdin.readline().split())

graph =[[] for _ in range(n+1)]
indegree = [0] * (n + 1)

for _ in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    indegree[child] += 1

result = topology_sort(graph, indegree)    

for value in result:
    print(value, end =" ")