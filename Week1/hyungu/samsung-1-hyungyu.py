n=int(input())
map=[list(map(int,input().split())) for _ in range(n)]
x, y=n//2, n//2
dx=[0,1,0,-1]
dy=[-1,0,1,0]

sandx=[
    [-1,1,-2,2,0,-1,1,-1,1],    #left
    [-1,-1,0,0,2,0,0,1,1],      #down
    [1,-1,2,-2,0,1,-1,1,-1],    #right
    [1,1,0,0,-2,0,0,-1,-1]      #up
]

sandy=[
    [1,1,0,0,-2,0,0,-1,-1],     #left
    [-1,1,-2,2,0,-1,1,-1,1],    #down
    [-1,-1,0,0,2,0,0,1,1],      #right
    [1,-1,2,-2,0,1,-1,1,-1]     #up
]

rate=[1,1,2,2,5,7,7,10,10]

def move(x,y,dir):
    value=0
    sum_value=0
    sand=map[x][y]
    for i in range(len(rate)):
        nx=x+sandx[dir][i]      #비율값으로 가는 좌표
        ny=y+sandy[dir][i]
        sand_move=(sand*rate[i]) // 100     #모래가 각 좌표에 가는 비율
        sum_value+=sand_move

        if not (0<=nx<n and 0<=ny<n):
            value+=sand_move    #나간 모래의 양
            continue
        map[nx][ny]+=sand_move  #안나갔다면 해당 좌표에 모래값 더해줌

    nx=x+dx[dir]    #알파 좌표
    ny=y+dy[dir]
    a=sand-sum_value    #알파에 있는 모래 양
    if not(0<=nx<n and 0<=ny<n):
        value+=a
    else:
        map[nx][ny]+=a
    
    map[x][y]=0     #굳이 있어야 할까?
    return value

def solve(x,y):
    value=0
    visited=[[False]*n for _ in range(n)]
    dir=-1
    while True:
        if x==0 and y==0:   #마지막 칸 오면 종료
            break
        visited[x][y]=True
        nd=(dir+1)%4
        nx=x+dx[nd]
        ny=y+dy[nd]

        if visited[nx][ny]:     #이미 방문 했을시
            nd=dir
            nx=x+dx[nd]
            ny=y+dy[nd]
        value+=move(nx,ny,nd)   #move 함수 호출하여 나간 모래값 더해줌
        x,y,dir=nx,ny,nd
    
    return value

result=solve(x,y)

print(result)