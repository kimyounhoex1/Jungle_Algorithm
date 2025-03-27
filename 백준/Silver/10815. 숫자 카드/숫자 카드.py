import sys

N = int(sys.stdin.readline())
N_list =[]

N_list = list(map(int, sys.stdin.readline().split()))

N_list.sort()
M = int(sys.stdin.readline())

M_list =[]

M_list = list(map(int, sys.stdin.readline().split()))


result_arr = []

for i in range(M):
    start = 0 
    end =  N-1
    mid = (start + end) // 2
    bool = False
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] > M_list[i]:
            end = mid-1
        elif N_list[mid] < M_list[i]:
            start = mid+1
        else:
            result_arr.append(1)
            bool = True
            break
    if not bool:
        result_arr.append(0)
    


for i in range(M):
    print(result_arr[i], end=" ")