n,k=map(int,input().split())
coin=[]

for _ in range(n):
    coin.append(int(input()))

dp=[0]*(k+1)
dp[0]=1 #제일 처음에 1인경우 다 경우가 1씩 되니까 그걸 충족시키기 위해

for i in coin:  #동전 종류마다
    for j in range(i,k+1):  #예를 들어 6원은 1원으로 만드는 경우 하나 + 4원 만들 수 있는 경우의수(+2만 하면 6이 되니까)
        dp[j]+=dp[j-i]

print(dp[k])