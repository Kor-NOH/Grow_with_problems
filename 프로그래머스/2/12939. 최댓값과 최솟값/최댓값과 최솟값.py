def solution(s):
    num_list = [int(num) for num in s.split()]
    max_num = max(num_list)
    min_num = min(num_list)
    answer = '{} {}'.format(min_num, max_num)
    return answer