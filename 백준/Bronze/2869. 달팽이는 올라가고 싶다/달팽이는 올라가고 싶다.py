import sys
import math

test_data = list(map(int, sys.stdin.readline().split()))

A = test_data[0]
B = test_data[1]
V = test_data[2]

print(math.ceil((V-A)/(A-B)) + 1)
    