from collections import deque


def bfs(start, max_floor, goal, up, down):
    queue = deque()
    queue.append((start, 0))
    visited = set()

    while queue:
        floor, depth = queue.popleft()

        if floor in visited:
            continue
        else:
            visited.add(floor)

        if floor == goal:
            return depth

        if floor + up <= max_floor:
            queue.append((floor + up, depth + 1))
        if floor - down > 0:
            queue.append((floor - down, depth + 1))

    return "use the stairs"


if __name__ == "__main__":
    F, S, G, U, D = map(int, input().split())
    print(bfs(S, F, G, U, D))
