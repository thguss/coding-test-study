def solution(id_list, report, k):
    listed = {}
    reporting = {}
    
    for user in report:
        u1, u2 = user.split(" ")
        if u1 in reporting.keys() and u2 in reporting[u1]:
            continue
        if u2 in listed.keys(): 
            listed[u2] += 1
        else: 
            listed[u2] = 1
        if u1 in reporting.keys():
            reporting[u1].append(u2)
        else: reporting[u1] = [u2]
    
    answer = []
    
    for u in id_list:
        cnt = 0
        if u in reporting.keys():
            for r in reporting[u]:
                if listed[r] >=k:
                    cnt += 1
        answer.append(cnt)
    
    return answer