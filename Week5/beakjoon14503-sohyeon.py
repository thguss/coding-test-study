from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dest = [[-1,0], [0,1], [1,0], [0,-1]]

queue = deque()
queue.append([r, c, d])

visited = [[0]*m for _ in range(n)]
visited[r][c] = 1

def searching(x, y, w):
  for t in range(1, 5):
    dx, dy = x + dest[(w-t)%4][0], y + dest[(w-t)%4][1]

    if 0 <= dx < n and 0 <= dy < m and not board[dx][dy] and not visited[dx][dy]:
      visited[dx][dy] = 1
      queue.append([dx, dy, w-1])
      return True

  return False

while queue:
  x, y, w = queue.popleft()

  if not searching(x, y, w):
    dx, dy = x - dest[w%4][0], y - dest[w%4][1]

    if 0<= dx < n and 0<= dy < m and not board[dx][dy]:
      queue.append([dx, dy, w])


answer = 0
for v in visited:
  answer += v.count(1)

print(answer)


