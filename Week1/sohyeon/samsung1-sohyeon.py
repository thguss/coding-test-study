c = int(input())
land = [list(map(int, input().split())) for _ in range(c)]

way = [[0, -1], [1, 0], [0, 1], [-1, 0]]

move, cnt, two, w = 0, 0, 2, 1
i, j = c//2, c//2

out = 0

while 1:
  n, m = i+way[move%4][0], j+way[move%4][1]

  sand = 0
  
  # 7%
  if 0<=n-1<c and 0<=m<c : land[n-1][m] += int(land[n][m]*0.07)
  else: out += int(land[n][m]*0.07)
  if 0<=n+1<c and 0<=m<c : land[n+1][m] += int(land[n][m]*0.07)
  else: out += int(land[n][m]*0.07)

  sand += 2 * int(land[n][m]*0.07)

  # 1%
  if 0<=i-1<c and 0<=j<c : land[i-1][j] += int(land[n][m]*0.01)
  else: out += int(land[n][m]*0.01)
  if 0<=i+1<c and 0<=j<c : land[i+1][j] += int(land[n][m]*0.01)
  else: out += int(land[n][m]*0.01)

  sand += 2 * int(land[n][m]*0.01)

  # 10%
  if 0<=n-1<c and 0<=m-1<c : land[n-1][m-1] += int(land[n][m]*0.1)
  else: out += int(land[n][m]*0.1)
  if 0<=n+1<c and 0<=m-1<c : land[n+1][m-1] += int(land[n][m]*0.1)
  else: out += int(land[n][m]*0.1)

  sand += 2 * int(land[n][m]*0.1)

  # 5%
  if 0<=n<c and 0<=m-2<c : land[n][m-2] += int(land[n][m]*0.05)
  else: out += int(land[n][m]*0.05)

  sand += int(land[n][m]*0.05)

  # 2%
  if 0<=n-2<c and 0<=m<c : land[n-2][m] += int(land[n][m]*0.02)
  else: out += int(land[n][m]*0.02)
  if 0<=n+2<c and 0<=m<c : land[n+2][m] += int(land[n][m]*0.02)
  else: out += int(land[n][m]*0.02)

  sand += int(land[n][m]*0.02)

  # a
  if 0<=n<c and 0<=m-1<c : land[n][m-1] += land[n][m]-sand
  else: out += land[n][m]-sand

  land[n][m] = 0

  if n==0 and m==1 : break

  i, j = n, m

  cnt += 1
  if cnt == w:
    cnt = 0
    move += 1
    two -= 1
  
  if two == 0:
    two = 2
    w += 1

print(out)