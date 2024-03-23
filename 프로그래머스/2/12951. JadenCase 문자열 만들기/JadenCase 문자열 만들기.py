def solution(s):
    answer = ''
    past = ''
    s_list = [str(n) for n in s]
    
    s_list[0] = s_list[0].upper()
    for i in range(1, len(s_list)):
        if past == ' ':
            s_list[i] = s_list[i].upper()
        else:
            s_list[i] = s_list[i].lower()
        past = s_list[i]

    for n in s_list:
        answer += n

    return answer