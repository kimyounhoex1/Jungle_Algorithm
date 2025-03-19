import sys

def Z(n, x, y):

    if n == 0:
        return 0
    return 2*(x%2) + (y%2) + 4*(Z(n-1, (int)(x/2), (int)(y/2)))
    #2 * (x%2) + (y%2) 의 의미는 모든 좌표를 (0,0), (0, 1), (1, 0),
    #  (1, 1)로 바꿔서 생각하는데, 
    # (1, n)에서 1은 *2로 가중치를 두는 것

    # Z(n-1, (int)(x/2), (int)(y/2)) 는 분할해서 나누었으면 한번
    #  진행할때마다 큰 박스에 4번 진행하기에 *4

n, x, y = (map(int, sys.stdin.readline().split()))

print(Z(n, x, y))
