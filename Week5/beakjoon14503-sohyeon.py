
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dest = [[-1,0], [0,1], [1,0], [0,-1]]

visited = [[0]*m for _ in range(n)]
visited[r][c] = 1

def fourSearching(r, c, d):
  for _ in range(4):
    dx, dy = r + dest[(d+3)%4][0], c + dest[(d+3)%4][1]

    if 0 <= dx < n and 0 <= dy < m and not board[dx][dy] and not visited[dx][dy]:
      visited[dx][dy] = 1
      d = (d+3)%4
      r, c = dx, dy
      return r, c, d
    
    d = (d+3)%4
  
  return False

cnt = 1

while True:
  res = fourSearching(r, c, d)

  if not res:
    bx, by = r - dest[d][0], c - dest[d][1]
    if 0 <= bx < n and 0 <= by < m and not board[bx][by]:
      r, c = bx, by
    else:
      break
  
  else:
    r, c, d = res


ans = 0
for v in visited:
  ans += v.count(1)
print(ans)