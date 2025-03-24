import sys

# 테스트 케이스 수 입력
test_case = int(sys.stdin.readline())

# 주어진 탑 배열 입력
given_data = list(map(int, sys.stdin.readline().split()))

# 결과를 저장할 리스트
result_list = []

# 탑을 저장할 스택
stack = []

# 탑들을 순차적으로 처리
for i in range(test_case):
    # 현재 탑의 높이
    current = given_data[i]
    
    # 스택에서 pop 하면서, 현재 탑보다 높은 탑을 찾아냄
    while stack and stack[-1][0] < current:
        stack.pop()
    
    # 만약 스택이 비어있다면, 신호를 받을 수 없으므로 0 추가
    if not stack:
        result_list.append(0)
    else:
        # 스택의 top에 있는 탑이 현재 탑보다 크므로, 신호를 받은 탑의 인덱스 추가
        result_list.append(stack[-1][1] + 1)  # 1-based index

    # 현재 탑을 스택에 추가 (현재 탑의 높이와 인덱스)
    stack.append((current, i))

# 결과 출력
print(*result_list)