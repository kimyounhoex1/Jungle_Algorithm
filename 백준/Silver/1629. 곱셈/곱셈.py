import sys

a, b, c = map(int, (sys.stdin.readline().split()))

def recur(a, b, c):
    if(b==1):
        return a%c
    else:
        k = recur(a, b//2, c)
        if b%2 != 0:
            return (k*k*a)%c
        else:
            return (k*k)%c

print(recur(a, b, c))
