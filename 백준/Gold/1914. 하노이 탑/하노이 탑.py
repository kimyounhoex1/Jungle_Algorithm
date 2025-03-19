import sys

inputN = int(sys.stdin.readline())


def hanoi(N, start, end):
    if N == 1:
        print(f"{start} {end}")
        return
    
    hanoi(N-1, start, 6-start-end)
    print(f"{start} {end}")
    hanoi(N-1, 6-start-end, end)

def binary_mul(n):
    num = 1
    for i in range(n):
        num = num*2
    
    return num

if inputN > 20:
    print(binary_mul(inputN) -1)
else:
    print(binary_mul(inputN) -1)
    hanoi(inputN, 1, 3)