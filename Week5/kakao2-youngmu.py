import sys


def clean(n, m, matrix, start_point, direction):
    delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    cleaned = 0
    r, c = start_point

    while True:
        if matrix[r][c] == 0:
            cleaned += 1
            matrix[r][c] = 2

        else:
            break

        canGo = False
        for idx in range(1, 5):
            dc, dr = delta[(direction + idx) % 4]

            if 0 <= dr + r < n and 0 <= dc + c < m and matrix[dr + r][dc + c] == 0:
                r, c = dr + r, dc + c
                canGo = True
                break

        if not canGo:
            dc, dr = delta[(direction + 2) % 4]

            if matrix[dr][dc] == 0:
                r, c = dr + r, dc + c
            else:
                return cleaned


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    r, c, d = list(map(int, input().split()))
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(clean(n, m, matrix, (r, c), d))
