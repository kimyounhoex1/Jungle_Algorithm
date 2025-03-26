import sys

# 보드 초기화
def init_board(N, apples):
    board = [[False] * N for _ in range(N)]
    init_apple(board, apples)
    return board

# 사과 자리 초기화
def init_apple(board, apples):
    for row, col in apples:
        board[row-1][col-1] = True
    return board

# 뱀 움직임 방향
snake_mode = ["Right", "Down", "Left", "Up"]

# 뱀 방향 변경
def change_direction(snake_mode, direction, change):
    mode_idx = snake_mode.index(direction)
    if change == "D":
        mode_idx += 1
        return snake_mode[mode_idx % 4]
    elif change == "L":
        mode_idx -= 1
        return snake_mode[mode_idx % 4]

# 뱀 움직이고, 자리 판별해서 종료
def snake_move(snake_point, direction, snake_mode, apples, N):
    global count
    # 뱀이 이동하는 방향에 따라 좌표 업데이트
    if direction == "Left":
        snake_point.insert(0, [snake_point[0][0], snake_point[0][1]-1]) 
    elif direction == "Down":
        snake_point.insert(0, [snake_point[0][0]+1, snake_point[0][1]]) 
    elif direction == "Right":
        snake_point.insert(0, [snake_point[0][0], snake_point[0][1]+1]) 
    elif direction == "Up":
        snake_point.insert(0, [snake_point[0][0]-1, snake_point[0][1]])

    # 벽에 부딪힌 경우
    if snake_point[0][0] < 0 or snake_point[0][1] < 0 or snake_point[0][0] >= N or snake_point[0][1] >= N:
        return False

    # 자기 자신과 부딪힌 경우
    if snake_point[0] in snake_point[1:]:
        return False

    # 사과를 먹은 경우, 꼬리는 자르지 않는다.
    if snake_point[0] not in apples:
        snake_point.pop()# 꼬리 자르기
    else:
        apples.remove(snake_point[0])

    # 게임 시간 증가 (1초씩)
    count += 1
    return True

# 게임 시작 함수
def game_start(snake_point, apples, commands, snake_mode, N):
    direction = "Right"
    # 게임 시간은 0초부터 시작
    global count
    count = 0
    command_idx = 0  # 방향 변경 명령의 인덱스

    while True:
        # 1초마다 뱀을 이동시킨다
        if not snake_move(snake_point, direction, snake_mode, apples, N):
            return False
        
        # 방향 변경 명령이 있다면 처리
        if command_idx < len(commands) and count == int(commands[command_idx][0]):
            direction = change_direction(snake_mode, direction, commands[command_idx][1])
            command_idx += 1

        # 1초 증가
        if command_idx >= len(commands) and not snake_point:
            break
        
    return True

# 메인 부분
snake_point = []
N = int(sys.stdin.readline())  # 보드 크기
K = int(sys.stdin.readline())  # 사과의 개수
apple_point = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())  # 방향 변환 횟수
commands = [sys.stdin.readline().split() for _ in range(L)]  # 방향 변환 명령

# 사과 위치 수정 (0-based indexing)
for i in range(len(apple_point)):
    apple_point[i][0] -= 1
    apple_point[i][1] -= 1

# 게임 보드 초기화
board = init_board(N, apple_point)

# 게임 시작
game_start([[0, 0]], apple_point, commands, snake_mode, N)
print(count + 1)  # 마지막 한 초를 더 추가하여 출력