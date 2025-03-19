import sys

array = []
sum = 0
for _ in range(9):
    data = (int)(sys.stdin.readline())
    array.append(data)
    sum += data
    

array.sort()

def sol(array, sum):
    for i in range(0, 9):
        for j in range(i+1, 9):
            temp_sum = sum
            # print(i, j)
            if(temp_sum-array[j]-array[i] == 100):
                array.remove(array[j])
                array.remove(array[i])
                return
                
# print(sum)
sol(array, sum)
# print('---------------')
for data in array:
    print(data)
