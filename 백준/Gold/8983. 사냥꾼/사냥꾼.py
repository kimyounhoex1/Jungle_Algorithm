import sys

M, N, L = map(int, sys.stdin.readline().split())

shooting_list = list(map(int, sys.stdin.readline().split()))

# animal_point = [[0] * N for _ in range(N)]
animal_point = []
for _ in range(N):
    animal_point.append(list(map(int,sys.stdin.readline().split())))
count = 0
for i in range(N):
    for j in range(M):
        max = animal_point[i][0] - animal_point[i][1] + L
        min = animal_point[i][0] + animal_point[i][1] - L

        if min <= shooting_list[j] and shooting_list[j] <= max:
            count += 1
            break

print(count)

