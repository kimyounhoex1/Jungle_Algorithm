import sys

N = (int)(sys.stdin.readline())


arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

result = [0, 0]

def func(second, first, size):
    temp = arr[second][first]
    for i in range(second, second + size):
        for j in range(first, first + size):
            if temp != arr[i][j]:
                return False
    
    return True


def recur_func(second, first, size):
    if func(second, first, size):
        result[arr[second][first]] += 1
    else:
        half = size // 2
        recur_func(second, first, half)
        recur_func(second+half, first, half)
        recur_func(second, first+half, half)
        recur_func(second+half, first+half, half)    

recur_func(0, 0, N)     
print(result[0])
print(result[1])