import sys
import math

def is_prime_number(number):
    if(number <= 1):
        return False
    if(number==2):
        return True
    prime_number = [2, 3, 5, 7, 11, 13, 
                    17, 19, 23, 29, 37, 
                    41, 43, 47, 53, 59, 
                    61, 67, 71, 73, 79, 
                    83, 89, 97]
    for target_number in prime_number:
        if (number%target_number == 0):
            if target_number == number:
                return True
            return False
    return True

test_case = (int)(sys.stdin.readline())
test_data = list(map(int, sys.stdin.readline().split()))
count = 0
for data in test_data:
    if(is_prime_number(data)):
        count+=1
    
print(count)

