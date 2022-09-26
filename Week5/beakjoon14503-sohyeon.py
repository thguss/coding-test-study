from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dest = [[-1,0], [0,1], [1,0], [0,-1]]

visited = [[0]*m for _ in range(n)]
visited[r][c] = 1

queue = deque()
queue.append([r, c, d])

cnt = 1

while queue:
  x, y, w = queue.popleft()

  for i in range(4):
    w = (w+3)%4

    dx, dy = x + dest[w][0], y + dest[w][1]

    if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and not board[dx][dy]:
      visited[dx][dy] = 1
      queue.append([dx, dy, w])
      break
      
    elif i == 3:
      bx, by = x - dest[w][0], y - dest[w][1]
      if 0 <= bx < n and 0 <= by < m and not board[bx][by]:
        queue.append([bx, by, w])
      else:
        break

ans = 0
for v in visited:
  ans += v.count(1)
print(ans)