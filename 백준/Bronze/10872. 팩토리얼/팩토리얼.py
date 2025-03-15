import sys

def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)

value = (int)(sys.stdin.readline())

print(factorial(value))