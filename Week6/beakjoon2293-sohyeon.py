n, k = map(int, input().split())
cost = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for c in cost:
  for i in range(c, k+1):
    dp[i] += dp[i-c]

print(dp)

print(dp[k])