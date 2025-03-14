import sys

numbers = [(int)(sys.stdin.readline()) for i in range(2)]

# print(input[0] * temp%10)
# temp = (int)(input[1]/10)
# print(input[0] * temp%10)
# temp = (int)(input[1]/10)
# print(input[0] * temp%10)

result = numbers[0]*numbers[1]

for i in range(3):
    temp = numbers[1]
    numbers[1] = (int)(numbers[1]/10)
    print(numbers[0] * (temp%10))
    
print(result)

