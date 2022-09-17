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
    
        if s1 > mid:  # 중간값보다 크면 빼내야 함.
            temp = queue1.popleft()
            s1 -= temp
            # 기존 queue1에 있던 값을 빼내는 것이므로 queue2에 삽입 X (queue1의 합을 판단하는 것이므로)

        else:         # 중간값보다 작으면 가져와야 함.
            temp = queue2.popleft()
            s1 += temp
            queue1.append(temp)
        
        ans += 1
            
    return -1