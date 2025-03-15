import sys

max = -1

temp_index = 101

for i in range(9):
    temp = (int)(sys.stdin.readline())
    if(max<temp):
        max = temp
        temp_index = i+1
print(max)
print(temp_index)