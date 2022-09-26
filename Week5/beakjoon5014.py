from collections import deque

f, s, g, u, d = map(int, input().split())

queue = deque()
queue.append([s, 0])

answer = []
visited = []

while queue:
  floor, cnt = queue.popleft()

  visited.append(floor)

  if floor == g:
    answer.append(cnt)

  if 0 < floor + u <= f and floor+u not in visited:
    queue.append([floor+u, cnt+1])
    visited.append(floor+u)
  if 0 < floor - d <= f and floor-d not in visited:
    queue.append([floor-d, cnt+1])
    visited.append(floor-d)

if not answer:
  print("use the stairs")
else:
  print(min(answer))
