import heapq
import math
from collections import deque


def solution(fees, records):
    answer = []
    default_time, default_fee, pivot_time, pivot_fee = fees
    calculate_dict = dict()

    for record in records:
        time, plate, type = record.split()
        if plate not in calculate_dict:
            calculate_dict[plate] = deque()
        calculate_dict[plate].append(time)

    for plate in calculate_dict:
        time = 0
        while len(calculate_dict[plate]) != 0:
            in_time = calculate_dict[plate].popleft()
            if len(calculate_dict[plate]) != 0:
                out_time = calculate_dict[plate].popleft()
            else:
                out_time = "23:59"

            in_h, in_m = list(map(int, in_time.split(":")))
            out_h, out_m = list(map(int, out_time.split(":")))

            time += (out_h - in_h) * 60 + (out_m - in_m)
        fee = default_fee
        if time > default_time:
            fee += math.ceil((time - default_time) / pivot_time) * pivot_fee

        answer.append((plate, fee))

    answer.sort()

    result = []
    for plate, price in answer:
        result.append(price)

    return result


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
