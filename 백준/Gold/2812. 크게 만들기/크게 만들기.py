import sys

N, K = map(int, sys.stdin.readline().split())

stack = ['0']

number = sys.stdin.readline()

count = 0
for digit in number:
    if stack[-1] < digit:
        while len(stack) > 0 and stack[-1] < digit and count <= K:
            stack.pop()
            count += 1
        stack.append(digit)
        continue
    else:
        stack.append(digit)
    


for i in range(N-K):
    print(stack[i], end="")

    