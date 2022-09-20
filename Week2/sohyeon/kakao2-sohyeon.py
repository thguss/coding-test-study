#### 효율성 실패 ####
def solution(board, skill):
    for s in skill:
        # type, (r1, c1)~(r2, c2) 범위, degree
        t, r1, c1, r2, c2, d = s
        if t == 1: d *= (-1)
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += d

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0: answer += 1
            
    return answer


#### 구글링 (누적합) ####
def solution2(board, skill):  
    visited = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    # type, (r1, c1)~(r2, c2) 범위, degree
    for t, r1, c1, r2, c2, degree in skill:
        visited[r1][c1] += degree if t==2 else (-1)*degree
        visited[r1][c2+1] += degree if t==1 else (-1)*degree
        visited[r2+1][c1] += degree if t==1 else (-1)*degree
        visited[r2+1][c2+1] += degree if t==2 else (-1)*degree
    
    for j in range(len(board[0])):
        for i in range(len(board)):
            visited[i+1][j] += visited[i][j]
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited[i][j+1] += visited[i][j]
    
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += visited[i][j]
            if board[i][j] > 0: answer += 1
            
    return answer