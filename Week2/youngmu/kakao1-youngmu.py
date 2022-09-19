from collections import deque


def solution(queue1, queue2):
    total_sum = (sum(queue1) + sum(queue2))

    if total_sum % 2 == 1:
        return -1

    goal = total_sum // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    length = len(q1) * 3
    cnt = 0

    for idx in range(length):
        if sum_q1 < sum_q2:
            value = q2.popleft()
            q1.append(value)
            sum_q1 += value
            sum_q2 -= value
        elif sum_q1 > sum_q2:
            value = q1.popleft()
            q2.append(value)
            sum_q1 -= value
            sum_q2 += value
        else:
            return cnt

        cnt += 1
        if (sum_q1 == goal) and (sum_q2 == goal):
            return cnt

    return -1
