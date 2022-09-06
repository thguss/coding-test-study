from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

#가장 큰 블록 찾기 dfs,bfs?
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt,rainbow_cnt=1,0
    blocks,rainbows=[[x,y]],[]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and a[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])
                
            elif 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and a[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    for x,y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks+rainbows]


def remove(block):
    for x,y in block:
        a[x][y] = -2


def gravity(a):
    for i in range(n-2, -1, -1):
        for j in range(n):
            if a[i][j] > -1:
                r = i
                while True:
                    if 0<=r+1<n and a[r+1][j] == -2:
                        a[r+1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break


def rotate(a):
    new_a=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-1-j][i]=a[i][j]
    return new_a


score = 0  # 점수


while True:
    # 2. 가장 큰 블록 찾기
    visited = [[0] * n for _ in range(n)]
    blocks = []  # 가능한 블록 그룹들 넣을 리스트
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = bfs(i, j, a[i][j])
                # block_info = [블록크기, 무지개블록 개수, 블록좌표]
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    # 3. 블록제거+점수더하기
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0]**2

    # 4. 중력
    gravity(a)

    # 5. 90회전
    a = rotate(a)

    # 6. 중력
    gravity(a)

print(score)