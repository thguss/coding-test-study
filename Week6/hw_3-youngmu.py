def solution(alp, cop, problems):
    dp = [[987654321 for _ in range(152)] for _ in range(152)]
    goal_alp = 0
    goal_cop = 0

    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem

        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)
    dp[alp][cop] = 0

    for a in range(alp, goal_alp + 1):
        for c in range(cop, goal_cop + 1):
            # Case1. 알고력 1 증가
            dp[min(a + 1, goal_alp)][c] = min(dp[min(a + 1, goal_alp)][c], dp[a][c] + 1)

            # Case 2. 코딩력 1 증가.
            dp[a][min(c + 1, goal_cop)] = min(dp[a][min(c + 1, goal_cop)], dp[a][c] + 1)

            # Case 3. 문제 풀기
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if a >= alp_req and c >= cop_req:
                    min_a = min(goal_alp, a + alp_rwd)
                    min_c = min(goal_cop, c + cop_rwd)
                    dp[min_a][min_c] = min(dp[min_a][min_c], dp[a][c] + cost)

    return dp[goal_alp][goal_cop]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
