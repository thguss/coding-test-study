from collections import deque
from itertools import combinations, permutations

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def find_without_roads(N, src_cow, dst_cow, roads):
    cr, cc = src_cow
    tr, tc = dst_cow
    queue = deque()
    queue.append((cr, cc))
    visited = set()

    while queue:
        r, c = queue.popleft()

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == (tr, tc):
            return True

        delta_idx = 0
        for dr, dc in delta:
            if 1 <= dr + r <= N and 1 <= dc + c <= N and not roads[delta_idx][r][c]:
                queue.append((dr + r, dc + c))
            delta_idx += 1

    return False


if __name__ == "__main__":
    N, K, R = list(map(int, input().split()))
    match_without_road = set()
    road_map = [[[False for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(4)]

    for _ in range(R):
        r1, c1, r2, c2 = list(map(int, input().split()))
        dr = r2 - r1
        dc = c2 - c1
        idx = delta.index((dr, dc))
        road_map[idx][r1][c1] = True
        road_map[(idx + 2) % 4][r2][c2] = True

    cows = [tuple(map(int, input().split())) for _ in range(K)]

    cows_cnt = 0
    for cow1, cow2 in combinations(list(range(len(cows))), 2):
        cows_cnt += 1

        if find_without_roads(N, cows[cow1], cows[cow2], road_map):
            match_without_road.add((cow1, cow2))

    print(cows_cnt - len(match_without_road))
