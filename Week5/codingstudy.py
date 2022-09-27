def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0
    inf = 1e9

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    graph = [[inf] * (max_cop + 1) for _ in range(max_alp + 1)]
    graph[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                graph[i + 1][j] = min(graph[i + 1][j], graph[i][j] + 1)
            if j + 1 <= max_cop:
                graph[i][j + 1] = min(graph[i][j + 1], graph[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp = min(i + alp_rwd, max_alp)
                    next_cop = min(j + cop_rwd, max_cop)
                    graph[next_alp][next_cop] = min(graph[next_alp][next_cop], graph[i][j] + cost)
    answer = graph[-1][-1]

    return answer