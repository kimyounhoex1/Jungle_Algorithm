import sys
# def qsort(array, left, right):
#     pl = left
#     pr = right

#     pivot = array[(pl + pr) // 2]

#     while pl <= pr:
#         while array[pl] < pivot: pl += 1
#         while array[pr] > pivot: pr -= 1
#         if(pl <= pr):
#             array[pl], array[pr] = array[pr], array[pl]
#             pl += 1
#             pr -= 1

#     if left < pr: qsort(array, left, pr)
#     if pl < right: qsort(array, pl, right)

# def quci_sort(array):
#     qsort(array, 0, len(array)-1)

array = []

test_case = (int)(sys.stdin.readline())

for i in range(test_case):
    array.append((int)(sys.stdin.readline()))

# quci_sort(array)

array.sort()
for i in range(len(array)):
    print(array[i])



