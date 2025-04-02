import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

distance = [10000000000] * (n+1)
queue = []

node_list = [[]for _ in range(n+1)]
for _ in range(m):
    data = list(map(int, sys.stdin.readline().split()))
    node_list[data[0]].append((data[1], data[2]))

# print(node_list)
# print(distance)
count = 0

def dijkstra(start, node_list, end):
    global count
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        weight, node = heapq.heappop(q)
        # print("node, weight = ", node, ", ", weight)
        # print(q)
        # print("------------------------------------")
        if node == end:
            count = weight    
            break
        if distance[node] < weight:
            continue
        
        for vertex in node_list[node]:
            cost = distance[node] + vertex[1]
            if cost < distance[vertex[0]]:
                distance[vertex[0]] = cost
                heapq.heappush(q, (cost, vertex[0]))

start, end = map(int, sys.stdin.readline().split())
dijkstra(start, node_list, end)

print(count)



