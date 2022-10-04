n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dest = [[1, 0], [0, 1], [0, -1], [-1, 0]]
dice = [0, 0, 0, 0, 0, 0]

def turn(dice, w):
  a, b, c, d, e, f = dice
  if w == 1:
    return [c, b, f, a, e, d]
  elif w == 2:
    return [d, b, a, f, e, c]
  elif w == 3:
    return [b, f, c, d, a, e]
  elif w == 4:
    return [e, a, c, d, f, b]
  
for o in order:
  dx, dy = x + dest[o%4][0], y + dest[o%4][1]

  if 0<= dx < n and 0<= dy < m:
    x, y = dx, dy

    dice = turn(dice, o)

    if not board[x][y]:
      board[x][y] = dice[0]
    else:
      dice[0] = board[x][y]
      board[x][y] = 0
    
    print(dice[-1])