def solution(s):
    answer = []
    zero_cnt = 0
    tran_cnt = 0
    
    while s != '1':
        tran_cnt += 1
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        s_len = len(s)
    
        s = bin(s_len)[2:]
            
    answer.append(tran_cnt)
    answer.append(zero_cnt)
    return answer