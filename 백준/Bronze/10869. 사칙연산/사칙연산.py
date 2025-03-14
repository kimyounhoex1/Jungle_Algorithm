import sys

a = list(map(int, sys.stdin.readline().split(" ")))

print(a[0] + a[1])
print(a[0] - a[1])
print(a[0] * a[1])
print((int)(a[0] / a[1]))
# print(a[0] / a[1])
print(a[0] % a[1])