import sys

test_case = list(sys.stdin.readline().split())

def reverse(str):
    rev_str = ""
    for i in range(len(str)):
        rev_str += str[len(str)-1-i]

    return rev_str

one_num = (int)(reverse(test_case[0]))
two_num = (int)(reverse(test_case[1]))

print(max(one_num, two_num))





