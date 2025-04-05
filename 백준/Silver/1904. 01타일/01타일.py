import sys

def bottom_up_solution(n):
    dp = [0] * 2
    dp[0] = 1
    dp[1] = 1
    
    if n == 0:
        return dp[0]
    elif n ==1 :
        return dp[1]

    for i in range(2, n+2):
        dp[i%2] = (dp[0] + dp[1])%15746

    return dp[(n)%2]

test_num = int(sys.stdin.readline())

print(bottom_up_solution(test_num))
    