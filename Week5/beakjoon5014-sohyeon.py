from collections import deque

f, s, g, u, d = map(int, input().split())

queue = deque()
queue.append([s, 0])

answer = -1
visited = [0] * (f+1)
visited[s] = 1

while queue:
  floor, cnt = queue.popleft()

  if floor == g:
    answer = cnt
    break

  if 0 < floor + u <= f and not visited[floor+u]:
    queue.append([floor+u, cnt+1])
    visited[floor+u] = 1
  if 0 < floor - d <= f and not visited[floor-d]:
    queue.append([floor-d, cnt+1])
    visited[floor-d] = 1

if answer == -1:
  print("use the stairs")
else:
  print(answer)
