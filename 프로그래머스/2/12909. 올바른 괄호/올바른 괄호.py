def solution(s):
    answer = True
    open_cnt = 0
    s_list = [str(a) for a in s]
    for a in s_list:
        if open_cnt < 0:
            answer = False
            break
        
        if a == '(':
            open_cnt += 1
        else:
            open_cnt -= 1
    
    if open_cnt != 0:
        answer = False
    
    return answer