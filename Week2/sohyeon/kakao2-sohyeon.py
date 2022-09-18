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