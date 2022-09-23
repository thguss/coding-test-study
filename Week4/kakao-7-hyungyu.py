import math

def solution(fees, records):
    answer = []
    nt,nf,ut,uf=fees
    dic={}
    
    for record in records:
        time,number,parking=record.split()
        hour,minute=map(int,time.split(':'))
        time=hour*60+minute
        number=int(number)
        
        if number in dic:
            dic[number].append([time,parking])
        else:
            dic[number]=[[time,parking]]
    
    carlist=list(dic.items())
    carlist.sort(key=lambda x:x[0])
    
    for car in carlist:
        t=0
        
        for c in car[1]:
            if c[1]=="IN":
                t-=c[0]
            else:
                t+=c[0]
        
        if car[1][-1][1]=="IN":
            t+=(23*60)+59
            
        if t<=nt:
            answer.append(nf)
        else:
            answer.append(nf+math.ceil((t-nt)/ut)*uf)
    
    return answer