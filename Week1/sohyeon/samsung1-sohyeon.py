c = int(input())
land = [list(map(int, input().split())) for _ in range(c)]

way = [[0, -1], [1, 0], [0, 1], [-1, 0]]
move, cnt, two, w = 0, 0, 2, 1
i, j = c//2, c//2
out = 0

def percentOne(x, y):
  cx, cy = (-1)*x, (-1)*y
  case1, case2 = [cx+y, cy+x], [cx-y, cy-x]
  return [case1, case2]

def percentTen(x, y):
  cx, cy = x, y
  case1, case2 = [cx+y, cy+x], [cx-y, cy-x]
  return [case1, case2]

def percentSeven(x, y):
  case1, case2 = [y, x], [(-1)*y, (-1)*x]
  return [case1, case2]

def percentTwo(x, y):
  case1, case2 = [2*y, 2*x], [(-2)*y, (-2)*x]
  return [case1, case2]


def tornado(n, m, c1, c2, p):
  result = 0
  if 0 <= n+c1[0] < c and 0 <= m+c1[1] < c : land[n+c1[0]][m+c1[1]] += int(land[n][m]*p)
  else: result += int(land[n][m]*p)
  if 0 <= n+c2[0] < c and 0 <= m+c2[1] < c : land[n+c2[0]][m+c2[1]] += int(land[n][m]*p)
  else: result += int(land[n][m]*p)

  return result


while 1:
  x, y = way[move%4][0], way[move%4][1]
  n, m = i+x, j+y

  sand = 0
  
  # 7%
  c1, c2 = percentSeven(x, y)
  out += tornado(n, m, c1, c2, 0.07)
  sand += 2 * int(land[n][m]*0.07)

  # 1%
  c1, c2 = percentOne(x, y)
  out += tornado(n, m, c1, c2, 0.01)
  sand += 2 * int(land[n][m]*0.01)

  # 10%
  c1, c2 = percentTen(x, y)
  out += tornado(n, m, c1, c2, 0.1)
  sand += 2 * int(land[n][m]*0.1)

  # 5%
  if 0 <= n+2*x < c and 0 <= m+2*y < c : land[n+2*x][m+2*y] += int(land[n][m]*0.05)
  else: out += int(land[n][m]*0.05)
  sand += int(land[n][m]*0.05)

  # 2%
  c1, c2 = percentTwo(x, y)
  out += tornado(n, m, c1, c2, 0.02)
  sand += 2 * int(land[n][m]*0.02)

  # a
  if 0<=n+x<c and 0<=m+y<c : land[n+x][m+y] += land[n][m]-sand
  else: out += land[n][m]-sand

  land[n][m] = 0

  if n==0 and m==0 : break

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

