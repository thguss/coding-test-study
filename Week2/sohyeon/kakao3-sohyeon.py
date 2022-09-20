import math

def isPrime(num):
    if not num or num == "1": return False

    num = int(num)
    
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0: return False
    
    return True

def solution(n, k):
    digit = ""
    
    while (n > 0):
        digit = str(n%k) + digit
        n //= k
    
    digit = digit.split("0")

    answer = 0
    
    for num in digit:
        if isPrime(num): answer += 1
        
    return answer