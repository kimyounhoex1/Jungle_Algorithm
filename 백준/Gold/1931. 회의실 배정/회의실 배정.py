import sys

testcase = int(sys.stdin.readline())

test_list = []
for i in range(testcase):
    test_list.append(list(map(int, sys.stdin.readline().split())))

test_list.sort(key=lambda x : (x[1], x[0]))

# for i in test_list:
#     print(i)

start = 0
end = 1
count = 1
while end < testcase:
    if test_list[start][1] <= test_list[end][0]:
        # print("start = ", test_list[start], "end = ", test_list[end])
        count += 1
        start = end
    end += 1

print(count)