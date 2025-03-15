import sys

test_input = list(map(int, sys.stdin.readline().split()))

test_size =  (int)(sys.stdin.readline())

y_position = [0, test_input[1]]
x_position = [0, test_input[0]]
for i in range(test_size):
    test_data = list(map(int, sys.stdin.readline().split()))
    if(test_data[0] == 0):
        y_position.append(test_data[1])
    else:
        x_position.append(test_data[1])

x_position.sort()
y_position.sort()

# test_case = (x_position+1) * (y_position+1)
extend = []

for i in range(len(x_position)-1):
    for j in range(len(y_position)-1):
        extend.append(
            (y_position[j+1] -y_position[j]) * 
            (x_position[i+1] - x_position[i]))
    
print(max(extend))