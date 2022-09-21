def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported_dict = dict()

    id_map = dict()
    for idx in range(len(id_list)):
        id_map[id_list[idx]] = idx

    for report_log in report:
        reporter, reported = report_log.split(" ")
        if reported not in reported_dict:
            reported_dict[reported] = set()
        reported_dict[reported].add(reporter)

    for reported in reported_dict:
        if len(reported_dict[reported]) >= k:
            for reporter in reported_dict[reported]:
                idx = id_map[reporter]
                answer[idx] += 1

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
