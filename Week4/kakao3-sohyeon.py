import math

def solution(fees, records):
    dictq = dict()
    for r in records:
        record = r.split()
        hour, minute = list(map(int, record[0].split(':')))
        if record[2]=='IN':
            if record[1] not in dictq.keys():
                dictq[record[1]] = (hour*60 + minute)*(-1)
            else:
                dictq[record[1]] = dictq[record[1]] - (hour*60 + minute)
        else:
            dictq[record[1]] = dictq[record[1]] + (hour*60 + minute)

    answer = []
    for (car, cost) in sorted(dictq.items()):
        if cost <= 0:
            cost = cost + (23*60 + 59)

        if cost <= fees[0]:
            answer.append(fees[1])
        else:
            over_fee = math.ceil((cost-fees[0])/fees[2])*fees[3]
            answer.append(fees[1]+over_fee)
        
    return answer