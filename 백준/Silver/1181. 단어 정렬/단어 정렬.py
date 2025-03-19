import sys

test_case = (int)(sys.stdin.readline())

array = []
for i in range(test_case):
    data = sys.stdin.readline()
    if data not in array:
        array.append(data)

sorted_list = sorted(array, key = lambda x: (len(x), x))

for data in sorted_list:
    print(data, end="")