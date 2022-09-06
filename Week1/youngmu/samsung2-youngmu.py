from collections import deque

DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
EMPTY = -2
BLACK = -1
RAINBOW = 0


def find_block(matrix, start_x, start_y):
    dfs = [(start_x, start_y)]
    visited = set()
    block_color = matrix[start_y][start_x]
    rainbow_size = 0

    while dfs:
        x, y = dfs.pop()

        if (x, y) not in visited:
            visited.add((x, y))

            if matrix[y][x] == RAINBOW:
                rainbow_size += 1

            for direction in DIRECTION:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < N and 0 <= new_y < N:
                    if matrix[new_y][new_x] == block_color:
                        dfs.append((new_x, new_y))
                    elif matrix[new_y][new_x] == RAINBOW:
                        dfs.append((new_x, new_y))

    return visited, rainbow_size


def destroy_block(matrix, block):
    for (x, y) in block:
        matrix[y][x] = EMPTY


def gravity(matrix):
    for x in range(N):
        line = deque()
        black_y = -1

        for y in range(N):
            if matrix[y][x] == BLACK:
                block_cnt = len(line)

                for line_idx in range(len(line)):
                    value = line.pop()
                    matrix[y - 1 - line_idx][x] = value

                for idx in range(black_y + 1, y - block_cnt):
                    matrix[idx][x] = EMPTY

                black_y = y

            elif matrix[y][x] != EMPTY:
                line.append(matrix[y][x])

        if len(line) != N and len(line) != 0:
            block_cnt = len(line)

            for line_idx in range(len(line)):
                value = line.pop()
                matrix[N - 1 - line_idx][x] = value

            for idx in range(black_y + 1, N - block_cnt):
                matrix[idx][x] = EMPTY


def rotate(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]


if __name__ == "__main__":
    matrix = [list(map(int, input().split())) for _ in range(N)]
    score = 0

    while True:
        # Step 1
        big_block = [set(), 0]
        visited = set()
        for y in range(N):
            for x in range(N):
                if matrix[y][x] > RAINBOW and (x, y) not in visited:
                    block, rainbow_size = find_block(matrix, x, y)
                    visited.update(block)

                    if len(block) < 2:
                        continue

                    if (len(big_block[0]) <= len(block)) and big_block[1] <= rainbow_size:
                        big_block[0] = block
                        big_block[1] = rainbow_size

        if len(big_block[0]) == 0:
            break

        score += len(big_block[0]) ** 2
        destroy_block(matrix, big_block[0])

        # Step 2
        gravity(matrix)

        # Step3
        matrix = rotate(matrix)
        gravity(matrix)

    print(score)
