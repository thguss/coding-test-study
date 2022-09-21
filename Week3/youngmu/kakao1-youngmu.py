import itertools


def solution(board, skill):
    cnt = 0

    for effect in skill:
        t, r1, c1, r2, c2, degree = effect

        if t == 1:
            degree *= -1

        for r_idx in range(r1, r2 + 1):
            board[r_idx][c1:c2 + 1] = [i + j for i, j in
                                       zip(board[r_idx][c1:c2 + 1], [degree for i in range(c1, c2 + 1)])]

    answer = 0

    for col in range(len(board)):
        for row in range(len(board[0])):
            if board[col][row] >= 1:
                answer += 1

    return answer
