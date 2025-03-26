import heapq
import sys

test_case = int(sys.stdin.readline())

array = []
for i in range(test_case):
    number = int(sys.stdin.readline())
    heapq.heappush(array, -number)
    if number==0:
       print(-heapq.heappop(array))
