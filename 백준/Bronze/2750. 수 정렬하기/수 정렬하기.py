import sys

test_case = (int)(sys.stdin.readline())

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if(arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr_list = []

for i in range(test_case):
    arr_list.append((int)(sys.stdin.readline()))

sort(arr_list)

for i in range(len(arr_list)):
    print(arr_list[i])