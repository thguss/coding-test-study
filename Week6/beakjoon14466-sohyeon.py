from collections import deque

n, k, r = map(int, input().split())

board = [[0]*(n+1) for _ in range(n+1)]
bridge = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    bridge[r1][c1].append((r2, c2))
    bridge[r2][c2].append((r1, c1))

def isVisit(x, y):
    visited = [[0]*(n+1) for _ in range(n+1)]
    
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx, ny = cx+dx, cy+dy
            if 0 < nx <= n and 0 < ny <= n and not visited[nx][ny]:
                if (nx, ny) not in bridge[cx][cy]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
           
    return visited

cows = [list(map(int, input().split())) for _ in range(r)]

res = 0

for i in range(len(cows)-1):
    visited = isVisit(cows[i][0], cows[i][1])
    for j in range(i+1, len(cows)):
        if not visited[cows[j][0]][cows[j][1]]:
            res += 1

print(res)
        
