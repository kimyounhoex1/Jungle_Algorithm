import sys

str = sys.stdin.readline().strip()

list_oper = []
list_number = []
i = 0
while str != "":
    # print(str)
    if "-" not in str and "+" not in str:
        list_number.append(int(str))
        break
    if str[i] == '-' or str[i] == '+':
        list_oper.append(str[i])
        list_number.append(int(str[:i]))
        str = str[i+1:]
        i = 0
    i += 1
# print(list_oper)
# print(list_number)

total = list_number[0]
i = 0
is_plus = True
for i in range(1, len(list_number)):
    if list_oper[i-1] == '-':
        is_plus = False
    if not is_plus:
        total = total - list_number[i]
    else:
        total = total + list_number[i]

print(total)