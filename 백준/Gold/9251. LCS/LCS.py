import sys
sys.setrecursionlimit(3000)

strA = sys.stdin.readline().strip()
strB = sys.stdin.readline().strip()

dp = [[None for _ in range(len(strB))] for _ in range(len(strA))]

# if strA[0] == strB[0]:
#     dp[0][0] = 0
# else:
#     dp[0][0] = 1

def recur(strA, strB, i, j):
    # for val in dp:
        # print(val)
    # print(i, " and", j)
    if i == -1 or j == -1:
        return 0
    if dp[i][j] != None:
        return dp[i][j]
    
    if strA[i] == strB[j]:
        dp[i][j] = recur(strA, strB, i-1, j-1) + 1            
    else:
        dp[i][j] = max(recur(strA, strB, i-1, j), recur(strA, strB, i, j-1))
    
    return dp[i][j]

print(recur(strA, strB, len(strA)-1, len(strB)-1))