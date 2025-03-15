import sys

size = (int)(sys.stdin.readline())

for i in range(size):
    stack = 1
    sum = 0
    str = sys.stdin.readline()
    is_true = False
    for i in range(len(str)):
        if(str[i] == 'O'):
            if(is_true):
                stack += 1
            is_true = True
            sum = sum + stack
            
        elif(str[i] == 'X'):
            is_true = False
            stack = 1
    print(sum)