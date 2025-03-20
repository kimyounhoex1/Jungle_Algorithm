import sys

## 최대공약수와 최소 공배수는 각 값의 공약수들만 알면 끝난다.
## 1, 소수도 판별해야 함, 소수가 메인 주제가 아니기에 코드는 설명 생략

### for문을 이용한 함수


def by_for(a: int, b: int):
    prime_number = [2, 3, 5, 7, 11, 13, 
                    17, 19, 23, 29, 37, 
                    41, 43, 47, 53, 59, 
                    61, 67, 71, 73, 79, 
                    83, 89, 97]
    
    def measure_list(number):
        list_numbers = []
        for i in range(0, len(prime_number), 1):
            while number % prime_number[i] == 0:
                list_numbers.append(prime_number[i])
                number /= prime_number[i]

        return list_numbers
    
    list_a = measure_list(a)
    list_b = measure_list(b)
    

    def greatest_common_divisor(list_A, list_B):
        a_point = 0
        b_point = 0

        result = 1
        while a_point < len(list_A) and b_point < len(list_B):
            if list_A[a_point] == list_B[b_point]:
                result *= list_A[a_point]
                a_point += 1
                b_point += 1
            
            else:
                if list_A[a_point] > list_B[b_point]:
                    b_point += 1
                else:
                    a_point += 1
        return result
    
    def least_common_multiple(list_A, list_B):
        a_point = 0
        b_point = 0

        result = 1
        while a_point < len(list_A) and b_point < len(list_B):
            if list_A[a_point] == list_B[b_point]:
                result *= list_A[a_point]
                a_point += 1
                b_point += 1
            else:
                if list_A[a_point] > list_B[b_point]:
                    result *= list_B[b_point]
                    b_point += 1
                else:
                    result *= list_A[a_point]
                    a_point += 1
        if(a_point == len(list_A)):
            while b_point < len(list_B):
                result *= list_B[b_point]
                b_point += 1
        
        else:
            while a_point < len(list_A):
                result *= list_A[a_point]
                a_point += 1
        
        return result
    
    return [greatest_common_divisor(list_a, list_b), least_common_multiple(list_a, list_b)]

### 재귀를 이용한 함수
def by_recur(a: int, b: int):
    if b == 0:
        return a
    return by_recur(b, a%b)
    


numberA, numberB = list(
    map(int, (sys.stdin.readline().split())))

# ret_list = by_for(numberA, numberB)
# print(ret_list[0])
# print(ret_list[1])

print(by_recur(numberA, numberB))
print((numberA*numberB)//by_recur(numberA, numberB))