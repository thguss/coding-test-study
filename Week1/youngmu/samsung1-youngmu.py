N = int(input())

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

X = 0
Y = 1

mask = {
    LEFT: {
        (-1, -2): 0.02,
        (0, -1): 0.01, (-1, -1): 0.07, (-2, -1): 0.1,
        (-3, 0): 0.05,
        (0, 1): 0.01, (-1, 1): 0.07, (-2, 1): 0.1,
        (-1, 2): 0.02
    },
    RIGHT: {
        (1, -2): 0.02,
        (0, -1): 0.01, (1, -1): 0.07, (2, -1): 0.1,
        (3, 0): 0.05,
        (0, 1): 0.01, (1, 1): 0.07, (2, 1): 0.1,
        (1, 2): 0.02
    },
    UP: {
        (0, -3): 0.05,
        (-1, -2): 0.1, (1, -2): 0.1,
        (-2, -1): 0.02, (-1, -1): 0.07, (1, -1): 0.07, (2, -1): 0.02,
        (-1, 0): 0.01, (1, 0): 0.01
    },
    DOWN: {
        (0, 3): 0.05,
        (-1, 2): 0.1, (1, 2): 0.1,
        (-2, 1): 0.02, (-1, 1): 0.07, (1, 1): 0.07, (2, 1): 0.02,
        (-1, 0): 0.01, (1, 0): 0.01
    }
}


def move(matrix, tornado_loc, direction):
    t_x, t_y = tornado_loc
    new_x, new_y = tornado_loc[X] + direction[X], tornado_loc[Y] + direction[Y]
    origin_dust = matrix[new_y][new_x]
    moved_dust = 0
    gone_dust = 0
    cur_mask = mask[direction]

    for dx, dy in cur_mask:
        moving_dust = int(origin_dust * cur_mask[dx, dy])
        moved_dust += moving_dust

        if 0 <= dx + t_x < N and 0 <= dy + t_y < N:
            matrix[dy + t_y][dx + t_x] += moving_dust
        else:
            gone_dust += moving_dust

    if 0 <= direction[X] + new_x < N and 0 <= direction[Y] + new_y < N:
        matrix[direction[Y] + new_y][direction[X] + new_x] += (origin_dust - moved_dust)
    else:
        gone_dust += (origin_dust - moved_dust)

    matrix[new_y][new_x] = 0

    tornado_loc[X] = new_x
    tornado_loc[Y] = new_y

    return gone_dust


if __name__ == "__main__":
    matrix = [list(map(int, input().split())) for i in range(N)]
    tornado_loc = [N // 2, N // 2]
    gone_dust = 0

    for i in range(1, N):
        if i % 2 == 1:
            for _ in range(i):
                gone_dust += move(matrix, tornado_loc, LEFT)
            for _ in range(i):
                gone_dust += move(matrix, tornado_loc, DOWN)
        else:
            for _ in range(i):
                gone_dust += move(matrix, tornado_loc, RIGHT)
            for _ in range(i):
                gone_dust += move(matrix, tornado_loc, UP)

    # 어짜피 N-1까지만 보면 됨
    for i in range(N - 1):
        gone_dust += move(matrix, tornado_loc, LEFT)

    print(gone_dust)
