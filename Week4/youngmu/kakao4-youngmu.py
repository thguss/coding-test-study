def solution(alp, cop, problems):
    INF = 9876543210
    # 최대 알고, 구현 찾기
    max_alp, max_cop = 0, 0
    problems_size = len(problems)
    for i in range(problems_size):
        if problems[i][0] > max_alp:
            max_alp = problems[i][0]
        if problems[i][1] > max_cop:
            max_cop = problems[i][1]

    # dp[i][j] : 알고력i, 코딩력j를 얻기위해 걸리는 최소 시간
    alp = min(alp, max_alp)  # 시작 알고력과 코딩력이 max보다 많을 수 있다
    cop = min(cop, max_cop)
    dp = [[INF for j in range(max_cop + 1)] for i in range(max_alp + 1)]
    dp[alp][cop] = 0

    for now_alp in range(alp, max_alp + 1):
        for now_cop in range(cop, max_cop + 1):
            # 1시간 이후
            if now_alp != max_alp:
                dp[now_alp + 1][now_cop] = min(dp[now_alp][now_cop] + 1, dp[now_alp + 1][now_cop])
            if now_cop != max_cop:
                dp[now_alp][now_cop + 1] = min(dp[now_alp][now_cop] + 1, dp[now_alp][now_cop + 1])

            # 문제이용
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= now_alp and cop_req <= now_cop:
                    after_alp = min(max_alp, now_alp + alp_rwd)
                    after_cop = min(max_cop, now_cop + cop_rwd)

                    dp[after_alp][after_cop] = min(dp[after_alp][after_cop], dp[now_alp][now_cop] + cost)

    # for a in dp:
    #     print(a)

    return dp[-1][-1]