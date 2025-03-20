import sys

test_case = (int)(sys.stdin.readline())
count = 0
def each_num(a: int):
    temp_arr = [None] * 2
    if a < 10:
        temp_arr[0] = 0
        temp_arr[1] = a
    
    temp_arr[0] = (a//10)%10
    temp_arr[1] = a%10

    return temp_arr

if test_case == 0:
    count = 1
else:
    temp_num = 0
    count = 0


    while temp_num != test_case:
        if(count == 0):
            temp_num = test_case
        numbers = each_num(temp_num)
        total = numbers[0]+numbers[1]
        temp_num = each_num(total)[1] + numbers[1]*10
        count +=1


print(count)
