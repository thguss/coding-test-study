### 테스트1 시간초과

def isPrime(num):
    if num == 1: return False
    for i in range(2, num):
        if num%i == 0: return False
    return True

def solution(n, k):
    res = ""
    while (n > 0):
        res += str(n%k)
        n //= k

    digit = ""
    for i in range(len(res)-1, -1, -1):
        digit += res[i]
    
    arr = digit.split("0")
    
    print(arr)
    answer = 0
    
    for num in arr:
        if not num: continue
        if isPrime(int(num)): answer += 1

    return answer