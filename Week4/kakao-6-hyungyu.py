def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dicReport={x:0 for x in id_list}
    
    for r in set(report):
        dicReport[r.split()[1]] +=1
        
    for r in set(report):
        if dicReport[r.split()[1]] >=k:
            answer[id_list.index(r.split()[0])]+=1
    
    return answer