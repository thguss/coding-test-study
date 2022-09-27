from collections import deque

f,s,g,u,d=map(int,input().split())
# f: 층수 s: 현재 위치 g: 목적지 u:위 d:아래
visited=[0]*(f+1)

def bfs(v):
    queue=deque([v])
    visited[v]=1
    while queue:
        v=queue.popleft()
        if v==g:
            print(visited[g]-1)
            return
        up,down=v+u,v-d
        if up<=f and visited[up]==0:
            queue.append(up)
            
            visited[up]=visited[v]+1
        if 0<down and visited[down]==0:
            queue.append(down)
            
            visited[down]=visited[v]+1
    
    print("use the stairs")

bfs(s)