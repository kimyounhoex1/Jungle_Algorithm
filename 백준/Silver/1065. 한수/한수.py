import sys

test_data = (int)(sys.stdin.readline())
# test_data_num = int(test_data)

def hansoo(number):
    if test_data < 100:
        return number
    
    count = 99
    for number in range(100, number+1, 1):
        delta =(int)((str)(number)[0]) - (int)((str)(number)[1])
        for i in range(1, 2):
            if(delta == (int)((str)(number)[i]) -  (int)((str)(number)[i+1])):
                count += 1
    return count

print(hansoo(test_data))

#h = []
# b = int(input())
# if b < 100:
#     print(b)
# else:
#     for i in range(100,b+1):
#         a = list(str(i))
#         if 2 * int(a[1]) == int(a[0]) + int(a[2]):
#             h.append(i)
#     print(99 + len(h))