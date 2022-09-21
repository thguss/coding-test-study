def solution(info, edges):
    edges_map = dict()
    visited = set()
    stack = [0]
    sheep = 1
    wolf = 0

    for edge in edges:
        if edge[0] not in edges_map:
            edges_map[edge[0]] = [edge[1]]
        else:
            edges_map[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)

            if current in edges_map:
                for child in edges_map[current]:
                    if info[child] == 0:
                        sheep += 1
                        stack.append(child)
                    else:
                        if sheep > wolf + 1:
                            wolf += 1
                            stack.append(child)

    return sheep


print (solution([0,0,1,1,1,0,1,0,1,0,1,1]	, [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))