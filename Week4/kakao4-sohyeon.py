import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    
    visited = [int(1e9)]*(n+1)
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        visited[start] = 0
        
        while q:
            intensity, num = heapq.heappop(q)
            
            # 산봉우리 도착 또는 새로 들어온 intensity가 더 큼
            if num in summits_set or intensity > visited[num]:
                continue
            
            for node, cost in graph[num]:
                new = max(intensity, cost)
                if visited[node] > new:
                    visited[node] = new
                    heapq.heappush(q, (new, node))
    
    summits.sort()
    summits_set = set(summits)
    
    for gate in gates:
        dijkstra(gate)
    
    num, intensity = 0, int(1e9)
    
    for summit in summits:
        if intensity > visited[summit]:
            num, intensity = summit, visited[summit]

    return [num, intensity]