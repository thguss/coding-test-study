def solution(alp, cop, problems):
    dp = [[987654321 for _ in range(152)] for _ in range(152)]
    dp[alp][cop] = 0
    goal_alp = 0
    goal_cop = 0

    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem

        if goal_alp < alp_req:
            goal_alp = alp_req
        if goal_cop < cop_req:
            goal_cop = cop_req

    for a in range(alp, goal_alp + 1):
        for c in range(cop, goal_cop + 1):
            # Case1. 알고력 1 증가
            if a + 1 <= goal_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            else:
                dp[goal_alp][c] = min(dp[goal_alp][c], dp[a][c] + 1)

            # Case 2. 코딩력 1 증가.
            if c + 1 <= goal_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)
            else:
                dp[a][goal_cop] = min(dp[a][goal_cop], dp[a][c] + 1)

            # Case 3. 문제 풀기
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if a >= alp_req and c >= cop_req:
                    if a + alp_rwd <= goal_alp and c + cop_rwd <= goal_cop:
                        dp[a + alp_rwd][c + cop_rwd] = min(dp[a + alp_rwd][c + cop_rwd], dp[a][c] + cost)

                    elif a + alp_rwd > goal_alp and c + cop_rwd > goal_cop:
                        dp[goal_alp][goal_cop] = min(dp[goal_alp][goal_cop], dp[a][c] + cost)

                    else:
                        if a + alp_rwd > goal_alp:
                            dp[goal_alp][c + cop_rwd] = min(dp[goal_alp][c + cop_rwd], dp[a][c] + cost)
                        else:
                            dp[a + alp_rwd][goal_cop] = min(dp[a + alp_rwd][goal_cop], dp[a][c] + cost)

    return dp[goal_alp][goal_cop]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
