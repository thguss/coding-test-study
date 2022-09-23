def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dicReport={x:0 for x in id_list}
    report=set(report)
    
    for r in report:
        dicReport[r.split()[1]] +=1
        
    for r in report:
        if dicReport[r.split()[1]] >=k:
            answer[id_list.index(r.split()[0])]+=1
    
    return answer