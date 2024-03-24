def solution(n):
    answer = 0
    goal = n+1

    n_binary_num = bin(n)[2:]
    n_binary_two_cnt = n_binary_num.count('1')
    
    while answer == 0:
        goal_binary_num = bin(goal)[2:]    
        goal_binary_two_cnt = goal_binary_num.count('1')
        
        if n_binary_two_cnt == goal_binary_two_cnt:
            answer = goal
            break
        
        else:
            goal += 1
            
    return answer