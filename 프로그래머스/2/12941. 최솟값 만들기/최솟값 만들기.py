def solution(A,B):
    answer = 0
    cnt = len(A)
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(cnt):
        answer += A[i] * B[i]

    return answer