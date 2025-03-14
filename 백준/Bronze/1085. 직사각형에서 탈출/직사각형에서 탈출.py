import sys

input = list((map(int, sys.stdin.readline().split(" "))))

length = input[2] - input[0]
height = input[3] - input[1]


def min(a, b):
    if a > b:
        return b
    else:
        return a

temp1 = min(length, height)
temp2 = min(input[0], input[1])

print(f"{min(temp1, temp2)}")

