import sys

target_case = (int)(sys.stdin.readline())

target_data = list(map(int, sys.stdin.readline().split()))
target_data.sort()

given_case = (int)(sys.stdin.readline())

given_data = list(map(int, sys.stdin.readline().split()))

def basic(target, given):
    for given in given_data:
        count = 0
        for target in target_data:
            if given == target:
                count += 1
        print(count)

def binary_search(target_list, given_list):
    for given in given_list:
        count = 0
        p_left = 0
        p_right = len(target_list) -1
        center = (p_left + p_right)//2
        while p_left <= p_right:
            center = (p_left + p_right)//2
            if target_list[center] == given:
                count += 1
                p_right = center -1
                break
            elif target_list[center] > given:
                p_right = center - 1
            else:
                p_left = center + 1  

            # if(p_left == p_right):
            #     break
        
        print(count)
                
binary_search(target_data, given_data)