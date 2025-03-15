import sys

map = dict()
for i in range(10):
    map[i] = 0

result = 1

for i in range(3):
    result *= (int)(sys.stdin.readline())

while result != 0:
    index = result%10
    map[index] += 1
    result =  (int)(result/10)

for i in range(10):
    print(map[i])