class Dice:
    def __init__(self):
        self.numbers = [0, 0, 0, 0, 0, 0]

    def move(self, direction, num):
        if direction == "UP":
            self.up(num)
        elif direction == "DOWN":
            self.down(num)
        elif direction == "RIGHT":
            self.right(num)
        elif direction == "LEFT":
            self.left(num)

    def up(self, num):
        tmp = self.numbers[0]

        for idx in range(4):
            self.numbers[idx] = self.numbers[idx + 1]
        self.numbers[3] = tmp

        if num != 0:
            self.numbers[3] = num

    def down(self, num):
        tmp = self.numbers[3]

        for idx in range(3, 0, -1):
            self.numbers[idx] = self.numbers[idx - 1]

        self.numbers[0] = tmp

        if num != 0:
            self.numbers[3] = num

    def right(self, num):
        tmp = self.numbers[5]

        self.numbers[5] = self.numbers[1]
        self.numbers[1] = self.numbers[4]
        self.numbers[4] = self.numbers[3]
        self.numbers[3] = tmp

        if num != 0:
            self.numbers[3] = num

    def left(self, num):
        tmp = self.numbers[4]

        self.numbers[4] = self.numbers[1]
        self.numbers[1] = self.numbers[5]
        self.numbers[5] = self.numbers[3]
        self.numbers[3] = tmp

        if num != 0:
            self.numbers[3] = num

    def get_top(self):
        return self.numbers[1]

    def get_bottom(self):
        return self.numbers[3]


if __name__ == "__main__":
    N, M, r, c, K = map(int, input().split())
    matrix = list()

    for _ in range(N):
        matrix.append((list(map(int, input().split()))))

    commands = list(map(int, input().split()))
    dice = Dice()
    directions = [(0, 0), (0, 1, 'RIGHT'), (0, -1, 'LEFT'), (-1, 0, 'UP'), (1, 0, 'DOWN')]

    for command in commands:
        dr, dc, d = directions[command]

        if 0 <= dr + r < N and 0 <= dc + c < M:
            r, c = (dr + r, dc + c)
            dice.move(d, matrix[r][c])
            if matrix[r][c] == 0:
                matrix[r][c] = dice.get_bottom()
            else:
                matrix[r][c] = 0
            print(dice.get_top())
