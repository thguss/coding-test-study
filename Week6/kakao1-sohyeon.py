
def solution(alp, cop, problems):
    alp_max, cop_max = 0, 0
    for problem in problems:
        alp_max, cop_max = max(alp_max, problem[0]), max(cop_max, problem[1])
    
    # 초기 알고력 & 코딩력이 요구 능력치보다 크면 0문제!
    alp, cop = min(alp, alp_max), min(cop, cop_max)
    
    dp = [[int(1e9)] * (cop_max + 1) for _ in range(alp_max + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, alp_max + 1):
        for j in range(cop, cop_max + 1):
            if i < alp_max:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < cop_max:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    alp_next, cop_next = min(alp_max, i + alp_rwd), min(cop_max, j + cop_rwd)
                    dp[alp_next][cop_next] = min(dp[alp_next][cop_next], dp[i][j] + cost)
                    
    return dp[alp_max][cop_max]

print(solution(0, 0, 	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))