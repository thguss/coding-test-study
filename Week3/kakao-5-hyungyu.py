dx=[-1,0,1,0]
dy=[0,-1,0,1]

def aturn(ax,ay,bx,by,cnt,board):
    if board[ax][ay]==0:
        return (1,cnt)
    winner=[]
    loser=[]
    canGo=False
    
    for i in range(4):
        nx=ax+dx[i]
        ny=ay+dy[i]
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny]==1:
            canGo=True
            newboard=[row[:] for row in board]
            newboard[ax][ay]=0
            isWin,turn=bturn(nx,ny,bx,by,cnt+1,newboard)
            if isWin==1:
                winner.append(turn)
            else:
                loser.append(turn)
    if canGo:
        if winner:
            return(0,min(winner))
        else:
            return(1,max(loser))
    else:
        return(1,cnt)
    
def bturn(ax,ay,bx,by,cnt,board):
    if board[bx][by]==0:
        return (1,cnt)
    winner=[]
    loser=[]
    canGo=False
    
    for i in range(4):
        nx=bx+dx[i]
        ny=by+dy[i]
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny]==1:
            canGo=True
            newboard=[row[:] for row in board]
            newboard[bx][by]=0
            isWin,turn=aturn(ax,ay,nx,ny,cnt+1,newboard)
            if isWin==1:
                winner.append(turn)
            else:
                loser.append(turn)
    if canGo:
        if winner:
            return(0,min(winner))
        else:
            return(1,max(loser))
    else:
        return(1,cnt)
        

def solution(board, aloc, bloc):
    ax,ay=aloc
    bx,by=bloc
    answer=aturn(ax,ay,bx,by,0,board)[1]
    
    return answer