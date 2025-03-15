import sys

test_case = (int)(sys.stdin.readline())

def average(list):
    sum = 0
    for i in range(1, list[0]+1, 1):
        
        sum += list[i]
    return (int)(sum/list[0])

for i in range(test_case):
    student_data = list(map(int, sys.stdin.readline().split()))
    avg = average(student_data)
    count = 0
    for i in range(1, student_data[0]+1, 1):
        if avg < student_data[i]:
            count += 1
    
    print(round(count/student_data[0] * 100, 3), "%")
