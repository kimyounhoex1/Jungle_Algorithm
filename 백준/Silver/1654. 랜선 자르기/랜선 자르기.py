import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

left, right = 1, max(lan)
result = 0

while left <= right:
    mid = (left + right) // 2
    # 잘린 랜선 개수 세기
    count = sum(x // mid for x in lan)
    if count >= N:
        result = mid        # 가능한 길이로 저장
        left = mid + 1      # 더 긴 길이도 시도
    else:
        right = mid - 1     # 너무 길면 줄이기

print(result)