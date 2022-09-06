n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j):
  num, size, rainbow, col, row = board[i][j], 0, 0, i, j # 블록 숫자, 크기, 무지개 수, 행, 열
  queue, visited, result = [], [[0]*n for _ in range(n)], []
  queue.append([i, j])
  visited[i][j] = 1

  while queue:
    x, y = queue.pop()
    result.append([x, y])
    size += 1
    for d in [[1,0], [0,1], [-1,0], [0,-1]]:
      dx, dy = x+d[0], y+d[1]
      if 0<=dx<n and 0<=dy<n and visited[dx][dy]==0 and (board[dx][dy]==0 or board[dx][dy]==num):
        queue.append([dx, dy])
        visited[dx][dy] = 1
        if board[dx][dy] == 0 : rainbow += 1 # 무지개
        else :
          if dx < col : col, row = dx, dy
          elif dx == col : 
            if dy < row : col, row = dx, dy

  return result, size, rainbow, col, row

def down():
  for i in range(n-2, -1, -1):
    for j in range(n-1, -1, -1):
      if board[i][j] == -1 : continue
      c = i
      while 1:
        if c+1>=n or board[c+1][j]!=-2: break
        board[c+1][j] = board[c][j]
        board[c][j] = -2
        c += 1


score = 0

while 1:
  group = [[], 0, 0, -1, -1]

  # 크기가 가장 큰 블록 그룹 찾기
  for i in range(n):
    for j in range(n):
      if board[i][j] == -1 or board[i][j] == 0 or board[i][j]==-2: continue
      res = list(bfs(i, j))
      if res[1] < 2 : continue # 그룹 크기는 2 이상
      # 그룹 크기
      if res[1] > group[1] : group = res
      elif res[1] == group[1] :
        # 무지개 블록 개수
        if res[2] > group[2] : group = res
        elif res[2] == group[2]:
          # 기준 블록의 행
          if res[3] > group[3] : group = res
          elif res[3] == group[3]:
            # 기준 블록의 열
            if res[4] > group[4]: group = res

  if group[0] == [] : break

  # 찾은 블록 제거하고 B**2 획득 (빈칸 == -2)
  for (x, y) in group[0]:
    board[x][y] = -2
  score += len(group[0])**2

  # 중력 작용
  down()

  # 90도 반시계 회전
  rotate = []
  for j in range(n-1, -1, -1):
    line = []
    for i in range(n):
      line.append(board[i][j])
    rotate.append(line)

  board = rotate

  # 2번째 중력 작용
  down()

print(score)