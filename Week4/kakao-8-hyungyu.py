from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_score=-1
    
    for com in combinations_with_replacement(range(11),n):
        ryan_info=[0]*11
        
        for i in com:
            ryan_info[10-i]+=1
        
        apeach,ryan=0,0
        for i in range(11):
            if info[i]==ryan_info[i]==0:
                continue
            elif info[i]>=ryan_info[i]:
                apeach+=10-i
            else:
                ryan+=10-i
        
        if ryan>apeach:
            score=ryan-apeach
            if score>max_score:
                max_score=score
                answer=ryan_info
    
    return answer