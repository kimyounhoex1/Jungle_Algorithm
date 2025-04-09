import sys

N, K = map(int, sys.stdin.readline().split())
## top_down 

## 내일 아침에 와서 무조건 1시간 안에 푼다. 일단 아이디어는 top down 방식으로는
## 배낭을 기준으로 있으면 넣고 없으면 가중치 없이 빼는 것이고, 계속 무게와 최대값을 고려해야 함 
## 배열은 2중배열을 사용해서 값을 갱신시키는 방법
dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]
def top_down(list, n, w):
    # print("n = ", n," w = ", w)
    # for i in dp:
    #     print(i)
    # print("----------------------")
    if n == 0:
        if w >= list[0][0]:
            return list[0][1]
        else:
            return 0
        
    if dp[n][w] != -1:
        return dp[n][w]
    
    if w - list[n][0] < 0:
        dp[n][w] = top_down(list, n-1, w)
    else: 
        dp[n][w] = max(top_down(list, n-1, w - list[n][0]) 
               + list[n][1], top_down(list, n-1, w))
    return dp[n][w]


## bottom_up

## 초기값을 알고 있으니까 초기값 기준으로 배낭에 물건이 하나씩 추가되었을때 무게를 더 더하고 가치도 더 더하자
# def recure_func_botton_up(n, w):



# bag_list = [[0, 0]]
bag_list = []
for i in range(N):
    bag_list.append(list(map(int, sys.stdin.readline().split())))

print(top_down(bag_list, N-1, K))