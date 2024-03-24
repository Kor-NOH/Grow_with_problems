def solution(n):
    now, past = 1, 0
    
    for i in range(2, n+1):

        now, past = now+past, now
    
    answer = now % 1234567
        
    return answer