import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

visited = [[False] * m for _ in range(n)]

board = []

for i in range(n):
    board_line = list(map(int, sys.stdin.readline().strip()))
    board.append(board_line)


def bfs(board, visited):
    queue = deque()
    
    queue.append((0, 0, 0))

    while queue:
        cur_point = queue.popleft()
        # print(queue)
        x, y = cur_point[0], cur_point[1]
        # print("x, y = ", x, ", ", y)
        # print("----------------------------")
        distance = cur_point[2]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        
        if board[x][y] == 0 or visited[x][y]:
            continue
        
        if x == n-1 and y == m-1:
            return distance+1
        visited[x][y] = True
        
        # if distance == 13:
        #     print("x, y = ",x , ", ", y)
        # if distance == 13:
        #     print("x, y = ",x , ", ", y)
        queue.append((x+1, y, distance+1))
        queue.append((x-1, y, distance+1))
        queue.append((x, y+1, distance+1))
        queue.append((x, y-1, distance+1))
        

    return distance

print(bfs(board, visited))