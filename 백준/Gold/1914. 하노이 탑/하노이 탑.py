import sys

inputN = int(sys.stdin.readline())


def hanoi(N: int, A: int, B: int, C: int):
    if (N == 1):
        print(A, C)
    else:
        hanoi(N-1, A, C, B)     # 처음 공통단계: A->B
        hanoi(1, A, B, C)       # 중간 공통단계: 하나만 A->C
        hanoi(N-1, B, A, C)     # 마지막 공통 단계: B->C


print(2**inputN-1)
if (inputN <= 20):
    hanoi(N=inputN, A=1, B=2, C=3)