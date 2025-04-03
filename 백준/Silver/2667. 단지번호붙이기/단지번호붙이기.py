import sys
from collections import deque
import heapq
test_case = int(sys.stdin.readline())

result = []
visited = []
for i in range(test_case):
    visited.append([])
    for _ in range(test_case):
        visited[i].append(False)

def bfs(board, start, n):
    queue = deque()
    queue.append(start)
    
    count = 0
    while queue:
        x, y = queue.popleft()

        if x < 0 or x >= n or y < 0 or y >= n:
            continue
        if visited[x][y]:
            continue
        if board[x][y] == '1':
            count += 1
            visited[x][y] = True
            queue.append((x, y+1))
            queue.append((x, y-1))
            queue.append((x+1, y))
            queue.append((x-1, y))
        

    if count != 0:
        heapq.heappush(result, count)

board = []
for i in range(test_case):
    board.append(sys.stdin.readline().strip())

for i in range(test_case):
    for j in range(test_case):
        bfs(board, (i, j), test_case)

result_num = len(result)
print(result_num)
for i in range(result_num):
    print(heapq.heappop(result))
