from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    sum1=sum(queue1)
    sum2=sum(queue2)
    total=sum1+sum2
    limit=len(queue1)+len(queue2)
    
    if total%2!=0:
        return -1
    
    while True:
        if sum1>sum2:
            target=queue1.popleft()
            queue2.append(target)
            sum1-=target
            sum2+=target
            answer+=1
        elif sum1<sum2:
            target=queue2.popleft()
            queue1.append(target)
            sum1+=target
            sum2-=target
            answer+=1
        else:
            break
        if answer==limit:
            answer =-1
            break
    
    return answer