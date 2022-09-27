n,m=map(int,input().split())
r,c,d=map(int,input().split())
graph=[]
visited=[[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]   #0:북 1:동 2:남 3:서
dy=[0,1,0,-1]

visited[r][c]=1
cnt=1

def turn_left():
    global d
    d-=1
    if d==-1:
        d=3

while True:
    isClear=0
    for i in range(4):
        turn_left() #왼쪽방향?? 북서남동 순
        nr=r+dx[d]
        nc=c+dy[d]

        if 0<=nr<n and 0<=nc<m and graph[nr][nc]==0:
            if visited[nr][nc]==0:
                visited[nr][nc]=1
                cnt+=1
                r=nr
                c=nc
                isClear=1
                break
    if isClear==0:
        if graph[r-dx[d]][c-dy[d]]==1:
            print(cnt)
            break
        else:
            r,c=r-dx[d],c-dy[d]