def min_coins(n, k, coins):
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, k + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[k] if dp[k] != float('inf') else -1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(min_coins(n, k, coins))