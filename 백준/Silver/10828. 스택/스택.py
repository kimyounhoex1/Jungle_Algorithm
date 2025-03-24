import sys

test_case = (int)(sys.stdin.readline())

stack = []
ptr = -1
for i in range(test_case):
    command = sys.stdin.readline().split()


    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    # if len(order) > 5:
    #     command, number = order.split()
    #     stack.append(number)
    # if order == "top":
    #     print(stack[-1])
    # if order == "size":
    #     print(len(stack))
    # if order == "empty":
    #     if stack[0] == None:
    #         print(1)
    #     else:
    #         print(0)
    # if order == "pop":
    #     stack.pop()


    
        
        
