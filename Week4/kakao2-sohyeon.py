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

    # 시간복잡도 처리 : 방문처리
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
        
        for i in range(11):
            if shoot.count(i) > info[i]: continue

            temp = []
            # 시간복잡도 개선 : 0발이지 않고, 0점이 아니고, 어피치보다 적은 발이면 어피치+1발로 queue 삽입
            if not shoot.count(i) and shoot.count(i) < info[i] and i != 10: 
                temp = sorted(shoot+[i]*(info[i]+1))
            else: 
                temp = sorted(shoot+[i])

            if temp and temp not in visited:
                visited.append(temp)
                queue.append(temp)

    answer = [0]*11

    if getScore(result, info) <= 0:
      answer = [-1]
    else:
      for score in result:
        answer[score] += 1

    return answer

print(solution(10, 	[0,0,0,0,0,0,0,0,3,4,3]))