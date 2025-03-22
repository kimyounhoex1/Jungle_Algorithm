import sys

def func(arr, mid):
    count =1
    start = arr[0]
    for i in range(1, len(arr)):
        if mid <= arr[i] - start:
            start = arr[i]
            count += 1
    
    return count

N, C = map(int, (sys.stdin.readline().split()))

arr = []
for i in range(N):
    arr.append((int)(sys.stdin.readline()))

arr.sort()

start = 1
end = arr[-1]

result = 0
while start <= end:
    mid = (start + end) // 2

    numbers = func(arr, mid)
    if(numbers >= C):
        result = max(result, mid)
        start = mid+1
    else: 
        end = mid - 1

print(result)