import sys

n = (int)(sys.stdin.readline())

for i in range(n):
    numbers = list(map(int, sys.stdin.readline().split()))
    print(numbers[0] + numbers[1])

