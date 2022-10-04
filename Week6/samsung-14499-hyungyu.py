n,m,x,y,k=map(int,input().split())

dice_map=[]
dx=[0,0,0,-1,1]       #동서북남(1234)
dy=[0,1,-1,0,0]
dice_num=[0,0,0,0,0,0]     #주사위 숫자 저장

for _ in range(n):
    dice_map.append(list(map(int,input().split())))     #지도

move=list(map(int,input().split()))     #이동하는 명령

def dice_cast(dir):      #주사위 굴리기
    n1,n2,n3,n4,n5,n6=dice_num[0],dice_num[1],dice_num[2],dice_num[3],dice_num[4],dice_num[5]
    if dir==1:  #동
        dice_num[0],dice_num[1],dice_num[2],dice_num[3],dice_num[4],dice_num[5]=n4,n2,n1,n6,n5,n3
    elif dir==2:    #서
        dice_num[0],dice_num[1],dice_num[2],dice_num[3],dice_num[4],dice_num[5]=n3,n2,n6,n1,n5,n4
    elif dir==3:    #북
        dice_num[0],dice_num[1],dice_num[2],dice_num[3],dice_num[4],dice_num[5]=n5,n1,n3,n4,n6,n2
    else:       #남
        dice_num[0],dice_num[1],dice_num[2],dice_num[3],dice_num[4],dice_num[5]=n2,n6,n3,n4,n1,n5


nx,ny=x,y

for i in move:
    nx+=dx[i]
    ny+=dy[i]

    if nx<0 or nx>=n or ny<0 or ny>=m:  #범위 벗어났을때
        nx-=dx[i]
        ny-=dy[i]
        continue       #왜 이걸 안해줬을까
    
    dice_cast(i)    #주사위 이동

    if dice_map[nx][ny]==0: #지도 칸이 0일떄
        dice_map[nx][ny]=dice_num[5]   #주사위 바닥면(dice_num[5]) 복사
    else:
        dice_num[5]=dice_map[nx][ny]    #지도 복사
        dice_map[nx][ny]=0      #칸은 0

    print(dice_num[0])  #이동할때마다 윗면 출력