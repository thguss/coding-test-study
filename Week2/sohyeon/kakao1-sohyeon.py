# 두 큐 합 같게 만들기
# 구글링 참고 ㅠㅠ -> 이진탐색 활용!

from collections import deque
   
def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    
    if (s1+s2)%2 != 0: return -1

    queue1, queue2 = deque(queue1), deque(queue2)
    
    ans, mid = 0, (s1+s2)/2
    
    while queue1 and queue2:
        if s1 == mid: return ans
    
        if s1 > mid:
            temp = queue1.popleft()
            s1 -= temp
        else:
            temp = queue2.popleft()
            s1 += temp
            queue1.append(temp)
        
        ans += 1
            
    return -1