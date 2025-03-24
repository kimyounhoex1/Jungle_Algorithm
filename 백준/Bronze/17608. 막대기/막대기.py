import sys

test_case = int(sys.stdin.readline())

stack = []
given_list = []

max = -100
for i in range(test_case):
    given_list.append(int(sys.stdin.readline()))

given_list.reverse()

for i in range(test_case):
    if(max < given_list[i]):
        max = given_list[i]
        stack.append(given_list[i])


print(len(stack))