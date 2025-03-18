import sys

test_case = (int)(sys.stdin.readline())
pos = [0] * test_case
flag_straight = [False] * test_case
flag_up = [False] * ((2*test_case)-1)
flag_down = [False] * ((2*test_case)-1)
    
count = 0

def set(i, n) -> None:
    global count
    
    for j in range(n):
        if (not flag_straight[j]
        and not flag_up[i+j]
        and not flag_down[i-j+n-1]):
            pos[i] = j
            if i == n-1:
                count += 1
            else:
                flag_straight[j] = flag_up[j+i] = flag_down[i-j+n-1] = True
                set(i + 1, n)
                flag_straight[j] = flag_up[j+i] = flag_down[i-j+n-1] = False


set(0, test_case)

print(count)
