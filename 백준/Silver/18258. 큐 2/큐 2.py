import sys

N= int(sys.stdin.readline())

arr = []
front = 0
back = 0

commands = []
for i in range(N):
    commands.append(sys.stdin.readline())
for i in range(N):
    command = commands[i]
    if 'push' in command:
        arr.append(command.split()[1])
        back += 1


    elif 'front' in command:
        if(front == back):
            print(-1)
        else:
            print(arr[front])
    
    elif 'back' in command:
        if(front == back):
            print(-1)
        else:
            print(arr[back-1])

    elif 'size' in command:
        print(back - front)
    
    elif 'empty' in command:
        if front == back:
            print(1)
        else:
            print(0)
        
    elif 'size' in command:
        print(back - front)
    elif 'pop' in command:
        if front == back:
            print(-1)
        else:
            print(arr[front])
            front += 1


