def solution(k, price, dp):
    dp[0] = 1

    for p in price:
        for j in range(1, k + 1):
            if j >= p:
                dp[j] += dp[j - p]


if __name__ == "__main__":
    n, k = map(int, input().split())
    price = list()
    dp = [0 for _ in range(k + 1)]

    for i in range(n):
        price.append(int(input()))

    solution(k, price, dp)

    print(dp[k])
