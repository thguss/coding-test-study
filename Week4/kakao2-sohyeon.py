from collections import deque

def getScore(res, info):
  a, b = 0, 0
  for i in range(11):
    if res.count(i) and res.count(i) > info[i]:
      a += 10-i
    elif info[i] and res.count(i) <= info[i]:
      b += 10-i

  return a-b

def solution(n, info):
    queue = deque()
    queue.append([])

    visited = []
    
    result = []
    
    while queue:
        shoot = queue.popleft()

        if len(shoot) == n:
            origin, new = getScore(result, info), getScore(shoot, info)
            if new > origin:
                result = shoot
            elif new == origin:
                for i in range(10, -1, -1):
                  if shoot.count(i) > result.count(i):
                    result = shoot
                    break
            continue
        
        for i in range(10):
            if shoot.count(i) > info[i]: continue
            temp = sorted(shoot+[i])
            if temp not in visited:
                visited.append(temp)
                queue.append(temp)

    answer = [0]*11

    if getScore(result, info) <= 0:
      answer = [-1]
    else:
      for score in result:
        answer[score] += 1

    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))