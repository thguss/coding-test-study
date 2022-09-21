def solution(n, k):
    answer = 0
    number=''
    while n:
        number=str(n%k)+number
        n=n//k
    
    number=number.split('0')
    
    for num in number:
        if len(num)==0:
            continue
        if int(num)<2:
            continue
        isPrime=True
        for i in range(2,int(int(num)**0.5)+1):
            if int(num)%i==0:
                isPrime=False
                break
        if isPrime:
            answer+=1
    return answer