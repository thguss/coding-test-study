from collections import deque

def solution(alp, cop, problems):
    maxA, maxC = 0, 0
    for p in problems:
        maxA = max(maxA, p[0])
        maxC = max(maxC, p[1])
    
    queue = deque()
    queue.append([alp, cop, 0])
    
    visited = [[0]*(maxC+1) for _ in range(maxA+1)]
    
    result = int(1e9)
    while queue:
        algo, code, cost = queue.popleft()
        
        if algo >= maxA and code >= maxC:
            result = min(result, cost)
            continue
        
        if algo < maxA and not visited[algo+1][code]:
            queue.append([algo+1, code, cost+1])
            visited[algo+1][code] = 1
        if code < maxC and not visited[algo][code+1]:
            queue.append([algo, code+1, cost+1])
            visited[algo][code+1] = 1
        
        for alg_req, cop_req, alp_rwd, cop_rwd, c in problems:
            if algo >= alg_req and code >= cop_req:
                tempA, tempC = algo+alp_rwd, code+cop_rwd
                if tempA > maxA: tempA = maxA
                if tempC > maxC: tempC = maxC
                if result > cost+c:
                    queue.append([tempA, tempC, cost+c])
                    visited[tempA][tempC] = 1
                    
    return result
